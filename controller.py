import storage
from version import Version


def init() -> None:
    pass


def update(dir: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    # get all file's hash values from stage
    stage.add_update(dir)
    for m in stage.modify_sequence:
        m.apply()

    storage.save_repo(repo)
    storage.save_stage(stage)


def update_add(src: str, dst: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    # TODO 

    storage.save_repo(repo)
    storage.save_stage(stage)


def transform(dir1: str, entry: str, msg: str, is_map: bool, dir2: str = ".") -> None:
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


def checkout(obj: str) -> None:
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