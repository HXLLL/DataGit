import storage
from repo import Repo
from stage import Stage
from version import Version


def init() -> None:
    repo = Repo()
    stage = Stage()

    storage.save_repo(repo)
    storage.save_stage(stage)


def update(dir: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    # get all file's hash values from stage
    stage.update(dir)

    storage.save_repo(repo)
    storage.save_stage(stage)


def add(src: str, dst: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    stage.add(dir)

    storage.save_repo(repo)
    storage.save_stage(stage)


def transform(dir1: str, entry: str, msg: str, is_map: bool, dir2: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    stage.transform(dir1, entry, is_map, dir2)

    storage.save_repo(repo)
    storage.save_stage(stage)


def commit(msg: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    repo.commit(stage, msg)
    stage = Version() # create a new stage

    storage.save_repo(repo)
    storage.save_stage(stage)


def checkout_v(obj: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    repo.checkout(obj)

    storage.save_repo(repo)
    storage.save_stage(stage)

def checkout_b(obj: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    repo.checkout(obj)

    storage.save_repo(repo)
    storage.save_stage(stage)


def save(obj: str) -> None:
    # load metadata
    repo.save(obj)
    # save metadata


def unsave(obj: str) -> None:
    # load metadata
    repo.unsave(obj)
    # save metadata


def adjust() -> None:
    repo.adjust()


def log() -> str:
    # get repo.log()
    # process
    return ''


def status() -> str:
    # get stage.status()
    # process
    return ''


def branch(name: str) -> str:
    # repo.branch()