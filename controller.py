import sys
import os
from storage import storage
from repo import Repo
from stage import Stage
from version import Version


def trans_path(dir: str) -> str:
    res = ''
    if os.path.isabs(dir):
        res = os.path.normpath(dir)
    else:
        res = os.path.normpath(os.path.join(os.getcwd(), dir))
    while res[:-1] == '.' or res[:-1] == '/':
        res = res[:-1]
    return res


def init() -> None:
    repo = Repo()
    repo.init()
    storage.save_repo(repo)

    stage = Stage()
    storage.save_stage(stage)


def update(dir:str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    dir = trans_path(dir)
    if os.path.exists(dir):
        if os.path.isdir(dir):
            stage.update(dir)
        else:
            print("fault: datagit update <dir>: <dir> should lead to a dir")
    else:
        print("fault: datagit update <dir>: <dir> should exist")

    storage.save_repo(repo)
    storage.save_stage(stage)


def add(src: str, dst: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    src = trans_path(src)
    dst = trans_path(dst)
    if os.path.exists(src):
        if os.path.isdir(src):
            stage.add(src, dst)
        else:
            print("fault: datagit add <src> <dst>: <src> and <dst> should lead to dir")
    else:
        print("fault: datagit add <src> <dst>: <src> and <dst> should exist")

    storage.save_repo(repo)
    storage.save_stage(stage)


def transform(dir1: str, entry: str, msg: str, is_map: bool, dir2: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    dir1 = trans_path(dir1)
    dir2 = trans_path(dir2)
    if os.path.exists(dir1) and os.path.exists(dir2):
        if os.path.isdir(dir1) and os.path.isdir(dir2):
            if not os.path.isabs(entry):
                entry_file = os.path.join(dir1, entry)
                if os.path.exists(entry_file):
                    if os.path.isfile(entry_file):
                        stage.transform(dir1, entry, is_map, dir2, msg)
                    else:
                        print("fault: datagit transform <dir1> <entry> -m <msg> [-s] [-d <dir2>]: <entry> should lead to"
                              " a file")
                else:
                    print("fault: datagit transform <dir1> <entry> -m <msg> [-s] [-d <dir2>]: <entry> should exist")
            else:
                print("fault: datagit transform <dir1> <entry> -m <msg> [-s] [-d <dir2>]: <entry> should be relative "
                      "path")
        else:
            print("fault: datagit transform <dir1> <entry> -m <msg> [-s] [-d <dir2>]: <dir1> <dir2> should lead to a dir")
    else:
        print("fault: datagit transform <dir1> <entry> -m <msg> [-s] [-d <dir2>]: <dir1> <dir2> should exist")

    storage.save_repo(repo)
    storage.save_stage(stage)


def commit(msg: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    if stage.empty():
        print("Nothing to commit")
        sys.exit(1)

    try:
        repo.commit(stage, msg)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
    print(msg)

    storage.save_repo(repo)
    storage.save_stage(stage)


def checkout_v(obj: int) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    repo.checkout(obj, False)
    stage.reset()

    storage.save_repo(repo)
    storage.save_stage(stage)


def checkout_b(obj: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    repo.checkout(obj, True)
    stage.reset()

    storage.save_repo(repo)
    storage.save_stage(stage)


def save(obj: int) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    try:
        repo.save(obj)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)


    storage.save_repo(repo)
    storage.save_stage(stage)


def unsave(obj: int) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    try:
        repo.unsave(obj)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    storage.save_repo(repo)
    storage.save_stage(stage)


def adjust() -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    repo.adjust()

    storage.save_repo(repo)
    storage.save_stage(stage)


def log() -> str:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    log_info = repo.log()

    storage.save_repo(repo)
    storage.save_stage(stage)
    return log_info


def status() -> str:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    status_info = repo.status()

    storage.save_repo(repo)
    storage.save_stage(stage)
    return status_info

def branch(name: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    if repo is None or stage is None:
        print("Error: Not in a valid repository")
        sys.exit(1)

    try:
        repo.branch(name)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    storage.save_repo(repo)
    storage.save_stage(stage)