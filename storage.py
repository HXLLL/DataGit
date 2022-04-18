import os
import shutil
from repo import Repo
from version import Version
import utils

class Storage:
    def __init__(self):
        pass

    def load_storage(self) -> None:
        """
        Nothing to do
        """
        pass

    def save_storage(self) -> None:
        """
        Nothing to do
        """
        pass

    def load_repo(self) -> Repo:
        """
        TODO: load repo from .datagit/repo
        """
        return Repo()

    def load_stage(self) -> Version:
        """
        TODO: load stage from .datagit/repo
        """
        return Version()

    def save_repo(self, repo: Repo) -> None:
        """
        TODO: save repo to .datagit/repo
        """
        pass

    def save_stage(self, stage: Version) -> None:
        """
        TODO: save repo to .datagit/repo
        """
        pass

    def create_repo(self) -> None:
        """
        Initialize a repo in current dir, 
        create all required directories for a repo
        """

        os.mkdir(".datagit")
        os.mkdir(".datagit/data")
        os.mkdir(".datagit/repo")
        os.mkdir(".datagit/stage")
        os.mkdir(".datagit/programs")
        os.mkdir(".datagit/versions")

    def save_file(self, file_name: str) -> str:
        """
        save a file \n
        file_name -- absolute path of the file to save
        """

        wd = self.get_working_dir()
        h = utils.get_hash(file_name)
        dst = os.path.join(wd, ".datagit/data/", h)
        shutil.copy(file_name, dst)
        return h

    def get_file(self, hash_value: str) -> str:
        """
        given a file's hash value, return its path.
        return -- relative path to working dir's root
        """

        return ".datagit/data/%s" % hash_value

    def get_working_dir(self) -> str:
        """
        get working directory's root
        return -- absolute dir of working dir's root
        """

        d = os.getcwd()
        while d != "/":
            if os.path.isdir(os.path.join(d, ".datagit")):
                break

        if d != "/":
            return d
        else:
            return None

    def save_transform(self, dir1: str) -> int:
        """
        save a transform program to the repo and assign an ID to it
        dir1 -- the program's absolute dir
        return -- the assigned id
        """

        wd = self.get_working_dir()
        program_dir = os.path.join(wd, ".datagit/programs")
        cnt = len(os.listdir(program_dir))
        id = cnt + 1
        dst = os.path.join(program_dir, "%d" % id)
        shutil.copytree(dir1, dst)
        return id

    def get_transform(self, id: int) -> str:
        """
        given a transform program's id, return its relative path
        return -- relative path to working dir's root
        """

        return ".datagit/programs/%d" % id

    def create_tmp_dir(self) -> str:
        """
        create a temp dir
        return -- absolute path to the temp dir
        !!! currently only support one temp dir at a time
        """
        wd = self.get_working_dir()
        tmp_dir = os.path.join(wd, ".datagit/tmp")
        if os.path.isdir(tmp_dir):
            shutil.rmtree(tmp_dir)
        os.mkdir(tmp_dir)
        return tmp_dir

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
