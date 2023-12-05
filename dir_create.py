from pathlib import Path

getDirectroy = Path.cwd()


def dir_create(pathname, folderName):
    full_path = pathname / folderName
    full_path.mkdir(parents=True, exist_ok=True)
    return full_path


dir_create(getDirectroy, "greatness")
