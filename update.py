from modify import Modify
from storage import storage
import utils
import os
import shutil

class Update(Modify):
    def __init__(self, add_list: list, remove_list: list):
        '''
        两个list的元素都是元组(path:str,file:Directory/Blob)
        path是从工作区的根目录开始的
        '''
        super().__init__()
        self.__add_list = add_list
        self.__remove_list = remove_list
        #保存add_list内的文件
        for item in self.__add_list:
            # print(item[1])
            Files = item[1].unfold(utils.get_working_dir())
            print(Files)
            for atuple in Files:
                h = storage.save_file(atuple[0])
                atuple[1].set_hash(h)
    
    def apply(self, working_dir):
        '''
        将Update对应文件增删应用到working_dir目录下
        '''
        for item in self.__add_list:
            Files = item[1].unfold(working_dir)
            for atuple in Files:
                file_path, _ = os.path.split(atuple[0])
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                git_file_name_0 = utils.get_working_dir()
                git_file_name_1 = storage.get_file(atuple[1].hash)
                shutil.copyfile(os.path.join(git_file_name_0, git_file_name_1), atuple[0])
            
        for item in self.__remove_list:
            path = os.path.join(working_dir, item[0])
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    def info(self) -> str:
        def file2str(f):
            return os.path.join(f[0], f[1].get_name())
        res = "add files: " + ", ".join(map(file2str, self.__add_list)) \
        + "\n" + "del files: " + ", ".join(map(file2str, self.__remove_list))
        return res
