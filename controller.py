import storage


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

    storage.save_repo(repo)
    storage.save_stage(stage)


def commit(msg: str) -> None:
    pass


def checkout(obj: str) -> None:
    pass


def save(obj: str) -> None:
    # load metadata
    # save metadata
    pass


def unsave(obj: str) -> None:
    # load metadata
    # save metadata
    pass


def adjust() -> None:
    pass


def log() -> str:
    pass


def status() -> str:
    pass


def branch(name: str) -> str:
    pass