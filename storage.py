import os
from repo import Repo
from version import Version

class Storage:
    def __init__(self):
        pass

    def load_storage(self) -> None:
        pass

    def save_storage(self) -> None:
        pass

    def create_repo(self) -> None:
        os.mkdir(".datagit")
        os.mkdir(".datagit/")
        pass

    def load_repo(self) -> Repo:
        return Repo()

    def load_stage(self) -> Version:
        return Version()

    def save_repo(self, repo: Repo) -> None:
        pass

    def save_stage(self, stage: Version) -> None:
        pass

    def save_file(self, file_name: str) -> File_info:
        pass

    def get_file(self, hash_value: str) -> str:
        """
        given a file's hash value, return its path.
        return value is relative path to working dir's root
        """
        return ".datagit/data/%s" % hash_value

    def get_working_dir(self) -> str:
        """
        return current repo's working dir's root
        """
        d = os.getcwd()
        while d != "/":
            if os.path.isdir(os.path.join(d, ".datagit")):
                break

        if d != "/":
            return d
        else:
            return None

    def save_transform(self, dir1: str, entry: str, isMap: str, dir2: str) -> int:
        pass

    def create_tmp_dir(self) -> str:
        pass

    def update_workingdir(self, version: Version, dir: str) -> None:
        pass

    def save_version(self, dir: str) -> None:
        pass

    def delete_version(self) -> None:
        pass


storage = Storage()
