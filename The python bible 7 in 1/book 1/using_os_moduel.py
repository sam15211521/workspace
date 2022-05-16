from time import sleep
import os

with open('help i am about to die.txt', 'w') as help_files:
    help_files.write('Help this computer is about to stop me from existing!')



os.mkdir('newdir')
os.chdir('newdir')
os.chdir('..')
sleep(5)
os.rmdir('newdir')
