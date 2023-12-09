from pathlib import Path

rawr = Path.cwd()


# List the folders in the directory
def dir_list(givenDirectory):
    real_list = []
    list_of_folders = Path(givenDirectory).iterdir()
    for folder in list_of_folders:
        if folder.is_dir() and (folder.name[0] == "."):
            continue
        elif folder.name == "venv":
            continue
        elif folder.name == "__pycache__":
            continue
        elif folder.is_dir():
            real_list.append(folder)
    return real_list



rawr = r'C:\Users\zEleceed\Desktop\POLY\Summit\Summit NF'

print(dir_list(rawr))