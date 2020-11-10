import argparse
import subprocess


def read(filePath):
    with open(filePath) as textFile:  # can throw FileNotFoundError
        out =  list(l.rstrip() for l in textFile.readlines())
    textFile.close()
    return out

def get_vivado_ver_str(lines):
    print(lines)






def main(file_path):
    lines = read(file_path)
    
    vivado_ver_str = get_vivado_ver_str(lines)
    


if __name__ == '__main__':
    
# parser = argparse.ArgumentParser()
# parser.add_argument('-f', '--file_path')
# args = parser.parse_args()
# 
# print(args.file_path)
# 
# main(args.file_path)

    main("C:\\PICs\\0243_pic\\projects\\viv_2018_3_test\\viv_2018_3_test.xpr")