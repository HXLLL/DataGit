import hashlib
import os.path

# from sklearn import utils

def get_working_dir() -> str:
    """
    get working directory's root
    return -- absolute dir of working dir's root
    """

    d = os.getcwd()
    while d != "/":
        if os.path.isdir(os.path.join(d, ".datagit")):
            break
        d = os.path.dirname(d)

    if d != "/":
        return d
    else:
        return None


def get_hash(file:str) -> str:
    f = open(file, 'rb')
    date = f.read()
    return hashlib.sha1(str(date)).hexdigest()

def in_working_dir(dir:str) -> bool:
    working_dir = get_working_dir()
    working_dir = os.path.abspath(working_dir)
    dir = os.path.abspath(dir)
    if len(working_dir) > len(dir):
        return False
    dir = dir[:len(working_dir)]
    if dir != working_dir:
        return False
    return True