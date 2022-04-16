from typing import List
from modify import Modify
from transfrom import Transform
from update import Update
import storage
from file_info import File_info


class Version():
    def __init__(self):
        self.modify_sequence = []

    

class Stage(Version):
    def __init__(self):
        super(Stage, self).__init__()
        self.modify_sequence = []

    # 仅stage调用
    def scan_different_files() -> list, list : 
        pass

    def add_update(self, dir: str) -> None:
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