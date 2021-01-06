### TRY/EXCEPT CASES
import os.path
from os import path
def is_digit(num):
    '''
    Tests if input is num. 
    '''
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            num = input("That was not an integer or your input exceeds the index.\n")
        
    return num

def is_path():
    '''
    Test if dir is a path.
    '''
    dir_input = input(f'Where do you want the files downloaded.\n')
    while True:
        if path.isdir(dir_input) == True:
            print(f'Directory exists.')
            break
        else:
            dir_input = input(f'That directory is invalid. You can check on terminal with command "pwd" or on CMD with "dir".\n')
    return dir_input

