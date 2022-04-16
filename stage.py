from typing import List
from modify import Modify
from transform import Transform
from update import Update
from storage import storage
from blob import File_info
from version import Version
from typing import Tuple

class Stage():
    def __init__(self):
        self.__modify_sequence = []

    def __scan_update() -> Tuple[list, list]:
        '''
        返回改动的add_list和remove_list
        两个list的元素都是元组(path:str,file:Directory/Blob)
        ''' 
        pass

    def update(self, dir: str) -> None:
        add_list, del_list = self.__scan_update()
        upd = Update(add_list, del_list)
        pass  # 还要做的事：把增加的文件利用storage.save_file方法实际保存下来。
    
    
    def transform(self, dir1, entry, isMap, dir2):
        dir_in_datagit = storage.save_transform(dir1, entry, isMap, dir2) # type: string
        m = Transform(dir_in_datagit, dir1, entry, isMap, dir2)
        self.modify_sequence.append(m)

        m.apply()

    def status(self):
        pass