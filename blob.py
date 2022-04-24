# from sympy import root
# from blob import Blob
from typing import List, Tuple
import os

class Blob:
    def __init__(self, name, hash=None) -> None:
        self.__name = name  # 文件名称
        self.__hash = hash  # 文件哈希值

    def get_name(self) -> str:
        return self.__name

    def get_hash(self) -> str:
        return self.__hash

    def unfold(self, root_path: str) -> List[Tuple[str, 'Blob']]:
        return [(os.path.join(root_path, self.__name), self)]
    
    def construct(self, working_dir: str) -> None:
        _, self.__name = os.path.split(working_dir)