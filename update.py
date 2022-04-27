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
            Files = item[1].unfold(os.path.join(utils.get_working_dir(), item[0]))
            # print(Files)
            for atuple in Files:
                # print('atuple[0]:', atuple[0])
                h = storage.save_file(atuple[0])
                atuple[1].set_hash(h)
    
    
    def apply(self, working_dir):
        '''
        将Update对应文件增删应用到working_dir目录下
        '''
        # print('apply:')
        # for a in self.__add_list:
        #     print(a[0], a[1].unfold('add_test'))
        # for a in self.__remove_list:
        #     print(a[0], a[1].unfold('del_test'))
        def move_file(base_path, afile) -> None:
            '''
            还原单个文件
            '''
            git_file_name_0 = utils.get_working_dir()
            git_file_name_1 = storage.get_file(afile.get_hash())
            shutil.copyfile(os.path.join(git_file_name_0, git_file_name_1), base_path)

        def move_dir(base_path, adir) -> None:
            '''
            将dir类下的目录结构还原,文件加入working_dir目录下
            '''
            if not os.path.exists(base_path):
                os.makedirs(base_path)
            
            for item in adir.get_dirs().values():
                move_dir(os.path.join(base_path, item.get_name()), item)
            
            for item in adir.get_files().values():
                move_file(os.path.join(base_path, item.get_name()), item)

        for item in self.__remove_list:
            path = os.path.join(working_dir, item[0], item[1].get_name())
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

        for item in self.__add_list:
            item_abs_path = os.path.join(working_dir, item[0], item[1].get_name())
            # print(item_abs_path, item[0], item[1].get_name())
            if item[1].get_type() == 'directory':
                move_dir(item_abs_path, item[1])
            else:
                move_file(item_abs_path, item[1])


    def info(self) -> str:
        def file2str(f):
            return os.path.join(f[0], f[1].get_name())
        res = "    add files: " + ", ".join(map(file2str, self.__add_list)) \
        + "\n" + "    del files: " + ", ".join(map(file2str, self.__remove_list))
        return res
