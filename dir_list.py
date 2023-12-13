from pathlib import Path

rawr = Path.cwd()


# List the folders in the directory
def dir_list(givenDirectory):
    real_list = []
    list_of_folders = Path(givenDirectory).iterdir()
    for folder in list_of_folders:
        if folder.is_dir() and not folder.name.startswith('.') and folder.name not in ["venv", "__pycache__"]:
            real_list.append(folder)
    return sorted(real_list)


print(dir_list(rawr))
