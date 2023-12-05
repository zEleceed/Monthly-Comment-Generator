from pathlib import Path

rawr = Path.cwd()
# List the folders in the directory
def dir_list(givenDirectory):
    list_of_folders = Path(givenDirectory).iterdir()
    for folder in list_of_folders:
        if folder.is_dir() and (folder.name[0] == "."):
            continue
        elif folder.is_dir():
            print(folder)


dir_list(rawr)