import hashlib
import os.path

from storage import Storage

class Utils:
    def __init__(self):
        pass


    def get_hash(self, file:str) -> str:
        f = open(file, 'rb')
        date = f.read()
        return hashlib.sha1(str(date)).hexdigest()

    def in_working_dir(self, dir:str) -> bool:
        working_dir = Storage.get_working_dir()
        working_dir = os.path.abspath(working_dir)
        dir = os.path.abspath(dir)
        if len(working_dir) > len(dir):
            return False
        dir = dir[:len(working_dir)]
        if dir != working_dir:
            return False
        return True