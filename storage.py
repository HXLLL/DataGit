import os
from repo import Repo
from version import Version
from stage import Stage
import utils
import pickle

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
        """
        load repo from .datagit/repo
        """
        repo_path = os.path.join(self.get_working_dir(), '.datagit', 'repo', 'repo.pk')
        with open(repo_path, 'wb') as repo_file:
            return pickle.load(repo_file)

    def load_stage(self) -> Stage:
        """
        load stage from .datagit/repo
        """
        stage_path = os.path.join(self.get_working_dir(), '.datagit', 'stage', 'stage.pk')
        with open(stage_path, 'wb') as stage_file:
            return pickle.load(stage_file)

    def save_repo(self, repo: Repo) -> None:
        """
        save repo to .datagit/repo
        """
        repo_path = os.path.join(self.get_working_dir(), '.datagit', 'repo', 'repo.pk')
        with open(repo_path, 'wb') as repo_file:
            pickle.dump(repo, repo_file)

    def save_stage(self, stage: Stage) -> None:
        """
        save stage to .datagit/stage
        """
        stage_path = os.path.join(self.get_working_dir(), '.datagit', 'stage', 'stage.pk')
        with open(stage_path, 'wb') as stage_file:
            pickle.dump(stage, stage_file)

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
    
    # 功能：返回当前工作区的根目录
    def get_root_path() -> str:
        pass

storage = Storage()
