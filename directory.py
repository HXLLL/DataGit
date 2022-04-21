from blob import Blob
from typing import List, Tuple, Union, Dict
import os

class Directory():
    def __init__(self, name: str) -> None:
        self.name: str = name      # 文件夹名称（不是路径）
        self.files: Dict[str, Union[Directory, Blob]] = {}  # key是子文件夹或子文件的名字

    def unfold(self, root_path: str) -> List[Tuple[str, Blob]]:
        '''
        功能：展开目录，返回一些元组(完整路径,对应的Blob)
        '''
        return [file.unfold(os.path.join(root_path, self.name)) 
                for file in self.files.values()]
    
    def enter(self, filename: str) -> Union['Directory', Blob, None]:
        '''
        功能:返回名字为filename的子目录或者子文件
        返回值:存在则返回Directory或Blob,不存在则返回None
        '''
        return self.files[filename] if filename in self.files.keys() else None
    
    def copy(self, new_dir):
        '''
        功能:复制new_dir的信息到self。用于就地更新目录树的某个节点而不改变父子关系。
        '''
        assert(self.name == new_dir.name)  # 如果名字变了，父亲就找不到self。
        self.files = new_dir.files

