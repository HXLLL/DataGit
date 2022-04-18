from typing import List
from modify import Modify
from transform import Transform
from update import Update
from storage import storage
from blob import File_info
from stage import Stage


class Version():
    def __init__(self, parent: 'Version', modify: Modify, message: str) -> None:
        self.__parent = parent
        self.__modify = modify
        self.__message = message
    
    def get_parent(self) -> 'Version':
        return self.__parent
    
    def get_modify(self) -> Modify:
        return self.__modify

    def get_message(self) -> str:
        return self.__message