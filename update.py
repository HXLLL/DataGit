from modify import Modify
import storage
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
            Files = item.unfold(storage.get_working_dir())
            for atuple in Files:
                atuple[1].hash = storage.save_file(atuple[1])
            
    
    def apply(self, working_dir):
        '''
        将Update对应文件增删应用到working_dir目录下
        '''
        for item in self.__add_list:
            Files = item.unfold(working_dir)
            for atuple in Files:
                file_path, file_name = os.path.split(atuple[0])
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                git_file_name_0 = storage.get_working_dir()
                git_file_name_1 = storage.get_file(atuple[1].hash)
                shutil.copyfile(os.path.join(git_file_name_0, git_file_name_1), atuple[0])
            
        for item in self.__del_list:
            path = os.path.join(working_dir, item)
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
