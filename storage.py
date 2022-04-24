import os
import shutil
from directory import Directory
from blob import Blob
import utils
import pickle

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

    def load_repo(self) -> 'Repo':
        """
        load repo from .datagit/repo
        """
        repo_path = os.path.join(utils.get_working_dir(), '.datagit', 'repo', 'repo.pk')
        with open(repo_path, 'rb') as repo_file:
            return pickle.load(repo_file)
        return None

    def load_stage(self) -> 'Stage':
        """
        load stage from .datagit/repo
        """
        stage_path = os.path.join(utils.get_working_dir(), '.datagit', 'stage', 'stage.pk')
        with open(stage_path, 'rb') as stage_file:
            return pickle.load(stage_file)
        return None

    def save_repo(self, repo: 'Repo') -> None:
        """
        save repo to .datagit/repo
        """
        repo_path = os.path.join(utils.get_working_dir(), '.datagit', 'repo', 'repo.pk')
        with open(repo_path, 'wb') as repo_file:
            pickle.dump(repo, repo_file)

    def save_stage(self, stage: 'Stage') -> None:
        """
        save stage to .datagit/stage
        """
        stage_path = os.path.join(utils.get_working_dir(), '.datagit', 'stage', 'stage.pk')
        with open(stage_path, 'wb') as stage_file:
            pickle.dump(stage, stage_file)

    def create_repo(self) -> None:
        """
        Initialize a repo in current dir, 
        create all required directories for a repo
        """
        if utils.get_working_dir() != None:
            # 仓库已存在，可能需要输出错误信息
            return
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

        wd = utils.get_working_dir()
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

    def save_transform(self, dir1: str) -> int:
        """
        save a transform program to the repo and assign an ID to it
        dir1 -- the program's absolute dir
        return -- the assigned id
        """

        wd = utils.get_working_dir()
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
        wd = utils.get_working_dir()
        tmp_dir = os.path.join(wd, ".datagit/tmp")
        if os.path.isdir(tmp_dir):
            shutil.rmtree(tmp_dir)
        os.mkdir(tmp_dir)
        return tmp_dir

    def recover_directory(self, d: Directory, dir: str):
        """
        dir is absolute path
        """
        wd = utils.get_working_dir()
        for name, f in d.get_files():
            if isinstance(f, Blob):
                h = f.hash
                f_dir = self.get_file(h)
                shutil.copy(f_dir, os.path.join(dir, name))
            else:
                raise "Error type in directory"
        
        for name, f in d.get_dirs():
            if isinstance(f, Directory):
                os.mkdir(os.path.join(dir, name))
                self.recover_directory(f, os.path.join(dir, name))
            else:
                raise "Error type in directory"
    
    def save_directory(self, d: Directory, dir: str):
        """
        dir is absolute path
        """
        for name, f in d.get_files():
            self.save_file(os.path.join(dir, name))

        for name, f in d.get_dirs():
            self.save_directory(f, os.path.join(dir, name))
        

    def update_workingdir(self, versionID: int, dir: str) -> None:
        wd = utils.get_working_dir()
        saved_version_dir = os.path.join(
            wd, ".datagit/versions/%d.pk" % versionID)
        directory = None
        with open(saved_version_dir, "rb") as f:
            directory = pickle.load(f)
        for d in os.listdir(dir):
            if d != '.datagit':
                shutil.rmtree(os.path.join(dir, d))
        self.recover_directory(directory, dir)

    def save_version(self, versionID: int, dir: str) -> None:
        d = Directory()
        d.construct(dir)
        self.save_directory(d, dir)

        wd = utils.get_working_dir()
        saved_version_dir = os.path.join(
            wd, ".datagit/versions/%d.pk" % versionID)
        with open(saved_version_dir, "wb") as f:
            pickle.dump(d, f)

    def delete_version(self, versionID: int) -> None:
        # TODO: actually remove saved files
        pass
        
    
    # 功能：返回当前工作区的根目录
    def get_root_path() -> str:
        pass


storage = Storage()
