from email.header import Header
from typing import Tuple, List, Union, Dict
import storage
from version import Version
from stage import Stage
from typing import List


class Repo:
    def __init__(self) -> None:
        init_version = Version(None, [], 'init', 1)
        self.versions: List[Version] = [init_version]
        self.saved_version: List[int] = [1]
        self.HEAD: Union[str, int] = 'main'
        self.detached_head: bool = False
        self.branch_map: dict[str, int] = {'main': 1}  # map branch name to version id
        self.version_map: dict[int, Version] = {1: init_version}  # map hash to version

    def init(self) -> None:
        storage.create_repo()

    def __new_version_id(self) -> int:
        return len(self.versions) + 1

    def commit(self, stage: Stage, message: str) -> None:
        """
        commit the stage, create a version with the stage
        save a stage to the repo's data structures
        """

        id = self.__new_version_id()
        v = stage.commit(id, message)
        self.version_map[id] = v
        self.versions.append(v)
        if not self.detached_head:
            b = self.HEAD
            assert type(b).__name__ == 'str'
            self.branch_map[b] = id
    
    # ------------------ checkout ---------------
    def __find_saved_dataSet(self, dest_version: Version) -> Tuple[Version, List[Version]]:
        """
        given a version *dest*, find the nearest saved version in *dest*'s ancestors,
        return that ancestor and the route from that ancestor to *dest*
        """

        route = []
        v = dest_version
        while not v.hash() in self.saved_version:
            route.append(v)
            pid = v.parent
            v = self.version_map[pid]
        route.reverse()
        return v, route

    def checkout(self, dst: Union[int, str], to_branch: bool) -> None: # op指示VersionID or branch_name
        """
        given a version ID or branch name, replace contents of the working dir with files of that branch
        """
        if to_branch:
            self.HEAD = dst
            self.detached_head = False
            dst = self.branch_map[dst]
        else:
            self.HEAD = dst

        dest_version = self.version_map[dst]
        src_version, route = self.__find_saved_dataSet(dest_version)
        working_dir = storage.get_working_dir()
        storage.update_workingdir(src_version.id, working_dir) #以存储版本的复原

        modify_sequence = []
        for v in route:
            modify_sequence += v.get_modify()
        for m in modify_sequence:
            m.apply(working_dir)

    # ------------------ save -----------------
    def save(self, VersionID: int) -> None:
        """
        save a version.
        """
        dest_version = self.version_map[VersionID] # exit if VersionID not exists
        src_version, route = self.__find_saved_dataSet(dest_version)
        tmp_dir = storage.create_tmp_dir()
        storage.update_workingdir(src_version.id, tmp_dir) #在某个位置将版本变换出来

        modify_sequence = []
        for v in route:
            modify_sequence += v.get_modify()
        for m in modify_sequence:
            m.apply(tmp_dir)

        storage.save_version(dest_version.id, tmp_dir)
        self.saved_version.append(VersionID) 

    # ------------------ unsave ---------------
    def unsave(self, VersionID: int) -> None:
        """
        unsave a version.
        """
        assert VersionID in self.saved_version

        storage.delete_version(VersionID)
        self.saved_version.delete(VersionID)

    # ------------------ adjust ---------------
    def find_suitable_versions(self) -> List[Version]:
        pass

    def adjust(self) -> None:
        pass

#         suitable_versions = find_suitable_versions()
#         for Version in suitable_versions:
#             self.save(Version)/self.unsave(Version)
    
# ------------------ log ---------------
    def log(self) -> str:
        res = ''
        for v in self.versions:
            res += "%s: %s" % (v.hash(), v.get_message())
        return res

    def status(self) -> str:
        stage = storage.load_stage()
        return stage.status()


# ------------------ branch ---------------
    def branch(self, branch_name) -> None:
        if self.detached_head:
            self.branch_map[branch_name] = self.HEAD
        else:
            self.branch_map[branch_name] = self.branch_map[self.HEAD]
        