import os
from datetime import datetime
from pathlib import Path

path = Path.cwd()

rawr = Path.cwd().iterdir()
for file in rawr:
    print(file)


class Program:
    def execute(self):
        pass