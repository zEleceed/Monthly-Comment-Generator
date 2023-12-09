import os
from dir_list import dir_list
from pathlib import Path
from dir_check import dir_check

currentDirectory = Path.cwd()

subDirectory = "MAG2"


def move_dir(current, new):
    new_path = current / new
    return os.chdir(new_path)

print(os.getcwd())
print(move_dir(currentDirectory, subDirectory))

print(os.getcwd())