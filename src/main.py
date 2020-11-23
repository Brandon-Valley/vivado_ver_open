import argparse
import subprocess
import os


XPR_VER_LINE_PREFIX = '<!-- Product Version: Vivado v'


def read(filePath):
    with open(filePath) as textFile:  # can throw FileNotFoundError
        out =  list(l.rstrip() for l in textFile.readlines())
    textFile.close()
    return out


def get_vivado_ver_str(file_path, lines):    
    if file_path.endswith('.xpr'):
        
        for line in lines:
            if line.startswith(XPR_VER_LINE_PREFIX):
                vivado_ver_str = line.split(XPR_VER_LINE_PREFIX)[1].split(' ')[0]
                return vivado_ver_str
    else:
        raise Exception("ERROR:  .xpr files only, cannot open:  " + file_path)
    
    
def get_env_var_name(vivado_ver_str):
    return 'VIVADO_BAT_PATH_' + vivado_ver_str.replace('.', '_')



def main(file_path):
    lines = read(file_path)
    
    vivado_ver_str = get_vivado_ver_str(file_path, lines)
    print('Vivado Version: ', vivado_ver_str)
    
    env_var_name = get_env_var_name(vivado_ver_str)
    print('Environment Variable: ', env_var_name)
    
    vivado_bat_path = os.environ[env_var_name]
    
    # cd to dir with file_path so extra Vivado files are not generated in this dir
    os.chdir(os.path.dirname(file_path))
    
    cmd = '{} {}'.format(vivado_bat_path, file_path)
    print('\nRunning cmd: ', cmd, '...')
    subprocess.call(cmd, shell = True)
    


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path')
    args = parser.parse_args()
      
    print(args.file_path)
      
    main(args.file_path)

#     main("C:\\PICs\\0243_pic\\projects\\viv_2018_3_test\\viv_2018_3_test.xpr")
    
    
    
    