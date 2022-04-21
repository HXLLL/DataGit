from blob import Blob
from typing import List, Tuple, Union, Dict
import os

class Directory():
    def __init__(self, name: str = '') -> None:
        self.name: str = name      # 文件夹名称（不是路径）
        self.files: Dict[str, Blob] = {}
        self.dirs: Dict[str, Directory] = {}

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
        
    def build_dict(self, working_dir: str) -> None:
        for item in os.listdir(working_dir):
            abs_path = os.path.join(working_dir, item)
            if os.path.isdir(abs_path):
                if item != '.datagit':
                    self.files[item] = Directory(item)
            else:
                self.files[item] = Blob(item)
    
    def construct(self, working_dir: str) -> None:
        _, self.name = os.path.split(working_dir)
        self.build_dict(working_dir)
        for item in self.files:
            item.construct(os.path.join(working_dir, item))
