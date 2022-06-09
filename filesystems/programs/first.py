from msilib.schema import Directory
import os

def current_path():
    print(f'the current directory is {os.getcwd()}')


os.chdir('../Files')

current_path()

def making_directories(dir):
    direcotry = dir
    parent_dir = os.getcwd()

    path = os.path.join(parent_dir, direcotry)

    os.mkdir(path)
    print(f'Directory {Directory} created')
    current_path()
    
making_directories('example1')

os.chdir('example1')

making_directories('exampleinexample')
    