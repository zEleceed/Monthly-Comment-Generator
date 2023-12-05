import os
from datetime import datetime
from pathlib import Path

path = Path.cwd() / "rawr"
print(path.is_dir())

os.chdir(path)

print(Path.cwd())