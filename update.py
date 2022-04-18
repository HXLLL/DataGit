from modify import Modify
import storage
import os
import shutil

class Update(Modify):
    def __init__(self, add_list: list, remove_list: list):
        super().__init__()
        self.__add_list = add_list
        self.__remove_list = remove_list
    
    def apply(self, working_dir):
        for item in self.add_list:
            Files = item.unfold(working_dir)
            for atuple in Files:
                file_path, file_name = os.path.split(atuple[0])
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                git_file_name_0 = storage.get_working_dir()
                git_file_name_1 = storage.get_file(atuple[1].hash)
                shutil.copyfile(os.path.join(git_file_name_0, git_file_name_1), atuple[0])
            
        for item in self.del_list:
            path = os.path.join(working_dir, item)
            if os.path.isdir(item):
                os.rmdir(path)
            else:
                os.remove(path)
