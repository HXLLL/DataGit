from email.header import Header
import storage
from version import Version

class TreeNode:
    def __init__(self, version: Version):
        self.version = version

class Repo:
    def __init__(self) -> None:
        self.Tree = []
        self.saved_version = []
        self.Head = []
        self.branch_map = {'BranchName':'ID'}
        self.version_map = {'ID':'TreeNode'}
        self.versino_message = {'ID':'String'}

    # ------------------ commit ---------------
    def save_version(self, Stage, message) -> TreeNode:
        version = Version(Stage, message)
        return TreeNode(version)

    def commit(self, Stage, message) -> None:
        TreeNode = self.save_version(Stage)
        self.Tree.append(TreeNode)
        Head = TreeNode
    
    # ------------------ checkout ---------------
    def find_saved_dataSet(self, destVersionID) -> int: #VersionID
        pass

    def checkout(self, VersionID/branch_name, op) -> None: # op指示VersionID or branch_name
        srcVersionID = self.find_saved_dataSet(VersionID)
        storage.update_workingdir(srcVersionID, working_dir) #以存储版本的复原

        route = []  # Versions from src to dest
        modify_sequence = []
        for Version in route:
            modify_sequence += Version.modify_sequence
        
        for Modify in modify_sequence:
            Modify.apply(working_dir)
        
        Head = "destVersion"

    # ------------------ save ---------------
    def save(self, VersionID) -> None:
        srcVersionID = self.find_saved_dataSet(VersionID)
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
        