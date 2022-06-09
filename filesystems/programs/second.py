import os

def curent_dir():
    print(f'The current directory is {os.getcwd()}')

directory = 'Kikhil'
parent_dir = os.chdir(f'{os.getcwd()}/../Files')

curent_dir()