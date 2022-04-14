import storage


def init() -> None:
    pass


def update(dir: str) -> None:
    repo = storage.load_repo()
    stage = storage.load_stage()

    stage.add_update(dir)
    for m in stage.modify_sequence:
        m.apply()

    storage.save_repo(repo)
    storage.save_stage(stage)

    pass
