from blob import Blob
from typing import List, Tuple
import os

class Directory():
    def __init__(self) -> None:
        self.file_list = []  # 元素类型可能是Directory或Blob
        self.name = 'null'   # 文件夹名称（不是路径）

    def unfold(self, root_path: str) -> List[Tuple[str, Blob]]:
        '''
        功能：展开目录，返回一些元组(完整路径,对应的Blob)
        '''
        return [file.unfold(os.path.join(root_path, self.name)) 
                for file in self.file_list]
