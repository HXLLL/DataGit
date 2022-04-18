from typing import List
from modify import Modify
from transform import Transform
from update import Update
from storage import storage
from blob import File_info
from stage import Stage


class Version():
    def __init__(self, parent: 'Version', modify: Modify, message: str) -> None:
        self.parent = parent
        self.modify = modify
        self.message = message
