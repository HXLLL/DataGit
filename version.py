from typing import List
from modify import Modify
from transform import Transform
from update import Update
from storage import storage
from blob import File_info
from stage import Stage


class Version():
    def __init__(self, stage: Stage, message: str, parent: 'Version') -> None:
        '''
        功能:复制一个stage,并添加commit信息,构造完的Version会被直接挂到提交树上
        '''
        self.__modify_sequence = stage.get_modify_sequence()
        self.__message = message
        self.__parent = stage.get_parent()

    def calc_hash() -> str:
        '''
        功能:计算Version的哈希值
        '''
        pass