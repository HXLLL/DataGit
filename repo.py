from email.header import Header
from typing import Tuple
import storage
from version import Version, Stage


class Repo:
    def __init__(self) -> None:
        self.versions: list[Version] = []
        self.saved_version: list[Version] = []
        self.HEAD: Version = None
        self.branch_map: dict[str, str] = {}  # map branch name to version id
        self.version_map: dict[str, Version] = {}  # map hash to version

    def commit(self, stage: Stage, message: str) -> None:
        """
        commit the stage, create a version with the stage
        save a stage to the repo's data structures
        """

        v = Version(stage, message)
        h = v.hash()
        self.version_map[h] = v
        self.versions.append(v)
        HEAD = v
    
    # ------------------ checkout ---------------
    def find_saved_dataSet(self, dest_version) -> Tuple[Version, list[Version]]:
        """
        given a version *dest*, find the nearest saved version in *dest*'s ancestors,
        return that ancestor and the route from that ancestor to *dest*
        """

        route = []
        v = dest_version
        while not v in self.saved_version:
            route.append(v)
            v = v.parent()
        route.reverse()
        return v, route


    # TODO: support checkout to a branch
    def checkout(self, VersionID: str, to_branch: bool) -> None: # op指示VersionID or branch_name
        """
        # currently not supporting checking out to a branch
        given a version ID, replace contents of the working dir with files of that branch
        """
        assert not to_branch

        dest_version = self.version_map[VersionID]
        src_version, route = self.find_saved_dataSet(dest_version)
        working_dir = storage.get_working_dir()
        storage.update_workingdir(src_version, working_dir) #以存储版本的复原

        modify_sequence = []
        for v in route:
            modify_sequence += v.get_modify_sequence()
        
        for m in modify_sequence:
            m.apply(working_dir)
        
        self.HEAD = dest_version

    # ------------------ save ---------------
    def save(self, VersionID) -> None:
        srcVersionID = self.find_saved_dataSet(VersionID)
        tmp_dir = storage.create_tmp_dir()
        storage.update_workingdir(srcVersionID, working_dir) #在某个位置将版本变换出来
        
        route = []  # Versions from src to dest
        modify_sequence = []
        for Version in route:
            modify_sequence += Version.modify_sequence
        
        for Modify in modify_sequence:
            Modify.apply(working_dir)
        
        storage.save_version(working_dir)
        
        self.saved_version += [VersionID]

# ------------------ unsave ---------------
    def unsave(self, VersionID) -> None:
        storage.delete_version(VersionID)

        self.saved_version.delete(VersionID)

# ------------------ unsave ---------------
    def find_suitable_versions(self) -> version_list:
        pass

    def adjust(self):
        suitable_versions = find_suitable_versions()
        for Version in suitable_versions:
            self.save(Version)/self.unsave(Version)
    
# ------------------ log ---------------
    def log(self) -> string:
        pass

# ------------------ branch ---------------
    def branch(self, branch_name):
        self.branch_map[branch_name] = self.Head
        