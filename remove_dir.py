from pathlib import Path
import shutil


print(Path.cwd())

nameFolder = input(f'Name the folder to remove: ')

shutil.rmtree(Path.cwd()/nameFolder)
