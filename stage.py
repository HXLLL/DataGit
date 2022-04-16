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
        m = Update()
        add_list_bypath, del_list_bypath = scan_different_files()
        for add_file in m.add_list:
            path_in_datagit = storage.save_file(add_file)
            
            m.add_list.append( File_info(path_in_datagit, add_file) ) # type: list[file_info]
            
        self.modify_sequence.append(m)
        for File_name in m.file_sequence:
            storage.savefile(File_name)
    
    
    def transform(self, dir1, entry, isMap, dir2):
        dir_in_datagit = storage.save_transform(dir1, entry, isMap, dir2) # type: string
        m = Transform(dir_in_datagit, dir1, entry, isMap, dir2)
        self.modify_sequence.append(m)

        m.apply()

    def status(self):
        pass