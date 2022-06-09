import os
path = os.getcwd()
new_path = f'{path}/../Files'
dir_list = os.listdir(new_path)
print(f'Files and directories in {new_path} :\n {dir_list}\n')
