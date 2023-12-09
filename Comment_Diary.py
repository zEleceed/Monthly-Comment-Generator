import os
from datetime import datetime
from pathlib import Path
from dir_list import dir_list


class Program:
    def __init__(self):
        pass

    def execute(self):
        print(f'Current Directory: {Path.cwd().name}')
        for i in dir_list(Path.cwd()):
            print(i.name)


        pass


hehe = Program()
hehe.execute()
