from pathlib import Path


# Check if the folder exists!
def dir_check(directoryName):
    parentPath = Path.cwd() / directoryName
    if Path(parentPath).exists():
        return True
    else:
        return False
