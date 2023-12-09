from pathlib import Path

getDirectory = Path.cwd()


def dir_create(pathname, folderName):
    full_path = pathname / folderName
    full_path.mkdir(parents=True, exist_ok=True)
    return full_path


fileName = input(f'Folder Name: ')
dir_create(getDirectory, fileName)
