import argparse

# parser = ArgumentParser()
# parser.add_argument("-f", "--file_path", dest="file_path_to_open",
#                     help="path to file to open in correct Vivado version, must be .xpr or .dcp", metavar="FILE_PATH_TO_OPEN")
# # parser.add_argument("-q", "--quiet",
# #                     action="store_false", dest="verbose", default=True,
# #                     help="don't print status messages to stdout")
# 
# args = parser.parse_args()
# 
# print(args)
# 
# print(args.file_path)



parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_path')
# parser.add_argument('-i', '--local_ip_repo_dir_path', default = "C:\\Users\\mt204e\\Documents\\test_ip_repo_2_CE4 - Copy (2)")
# parser.add_argument('-r', '--repo_remote_url'       , default = 'https://ba-bit.web.boeing.com/scm/mnfcf/tsm15.git')
# parser.add_argument('-a', '--app_id'                , default = 'None')
# parser.add_argument('-s', '--skip_ip_update'        , default = 'False')
args = parser.parse_args()

print(args.file_path)

# setup_new_repo(
#                args.repo_type, 
#                args.local_ip_repo_dir_path,
#                args.repo_remote_url,
#                args.app_id,
#                args.skip_ip_update
#               )