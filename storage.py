from file_info import File_info
from repo import Repo
from version import Version

class Storage:
    def __init__():
        pass

    def load_storage() -> None:
        pass

    def save_storage() -> None:
        pass

    def load_repo() -> Repo:
        return Repo()

    def load_stage() -> Version:
        return Version()

    def save_repo(repo: Repo) -> None:
        pass

    def save_stage(stage: Version) -> None:
        pass

    def save_file(file_name: str) -> File_info:
        pass


storage = Storage()
