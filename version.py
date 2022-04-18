from typing import List
from modify import Modify
from transform import Transform
from update import Update
from storage import storage
from blob import File_info
from stage import Stage
from typing import List


class Version():
    def __init__(self, id: int, parent: 'Version', modify_sequence: List[Modify], 
                 message: str) -> None:
        self.id = id
        self.parent = parent
        self.modify_sequence = modify_sequence
        self.message = message
