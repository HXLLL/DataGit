from typing import List
from modify import Modify
from transform import Transform
from update import Update
from storage import storage
from blob import Blob
from version import Version
from typing import Tuple

class Stage():
    def __init__(self):
        self.__modify_sequence = []

    def __scan_update(self) -> Tuple[list, list]:
        '''
        返回改动的add_list和remove_list
        两个list的元素都是元组(path:str,file:Directory/Blob)
        path是从工作区的根目录开始的
        ''' 
        pass

    def update(self, dir: str) -> None:
        add_list, del_list = self.__scan_update()
        upd = Update(add_list, del_list)
        # 还没写完
    
    def add(self, src_path: str, dst_path: str):
        pass
    
    def transform(self, dir1, entry, isMap, dir2):
        # 这里是之前写的伪代码，还没改
        dir_in_datagit = storage.save_transform(dir1, entry, isMap, dir2) # type: string
        m = Transform(dir_in_datagit, dir1, entry, isMap, dir2)
        self.modify_sequence.append(m)

        m.apply()
    
    def commit(self, message: str) -> Version:
        pass

    def status(self):
        pass