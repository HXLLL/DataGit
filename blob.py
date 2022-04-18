from sympy import root
from blob import Blob
from typing import List, Tuple
import os

class Blob:
    def __init__(self) -> None:
        self.name = 'null'  # 文件名称
        self.hash = 'null'  # 文件哈希值

    def unfold(self, root_path: str) -> List[Tuple[str, Blob]]:
        return [(os.path.join(root_path, self.name), self)]