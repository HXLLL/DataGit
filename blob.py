from sympy import root
from blob import Blob
from typing import List, Tuple
import os

class Blob:
    def __init__(self, name, hash=None) -> None:
        self.name = name  # 文件名称
        self.hash = hash  # 文件哈希值

    def unfold(self, root_path: str) -> List[Tuple[str, Blob]]:
        return [(os.path.join(root_path, self.name), self)]
    
    def construct(self, working_dir: str) -> None:
        _, self.name = os.path.split(working_dir)