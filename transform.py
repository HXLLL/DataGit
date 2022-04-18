from xmlrpc.client import boolean
from modify import Modify
from directory import Directory
import storage
import os

class Transform(Modify):
    def __init__(self, isMap: int, script_dir: str, script_entry: str, script_working_dir: str) -> None:
        # 这里存储的细节还要改
        super().__init__()
        self.__isMap = isMap
        self.__script_dir = script_dir                  #绝对
        self.__script_entry = script_entry              #绝对
        self.__script_working_dir = script_working_dir  #相对
        self.__id = storage.save_transform(script_dir)
    
    def apply(self, working_dir):
        git_script_dir = os.path.join(storage.get_working_dir(), storage.get_transform(self.__id))
        git_script_entry = os.path.join(git_script_dir, self.__script_entry)
        # .datagit内script_entry的绝对路径

        if self.__isMap == 0:
            cmd = git_script_entry + " " + os.path.join(working_dir, self.__script_working_dir)
            os.system(cmd)
        else:
            tmp_directory = Directory(self.__script_working_dir)
            Files = tmp_directory.unfold(working_dir)
            for path, _ in Files:
                cmd = git_script_entry + " " + path
                os.system(cmd)
