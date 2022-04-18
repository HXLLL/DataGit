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
        self.root_path = storage.get_working_dir()  # 这需要storage比Stage先初始化

    def __scan_update(self) -> Tuple[list, list]:
        '''
        返回改动的add_list和remove_list
        add_list的元素都是元组(path:str,file:Directory/Blob)
        remove_list的元素是path:str
        path是从工作区的根目录开始的
        '''
        pass

    def update(self, dir: str) -> None:
        add_list, del_list = self.__scan_update()
        for path, _ in add_list:
            storage.save_file(path)
        upd = Update(add_list, del_list)
        self.__modify_sequence.append(upd)
        # 还没写完
    
    def add(self, src: str, dst: str):
        '''
        参数都是绝对路径
        '''

        '''
        1.检查dst是否重名
        2.建dst文件夹
        3.把src里面的东西扔到dst里面
        4.建立dst文件夹的Directory结构
        5.把dir结构扔到modify_sequence里面
        '''
    
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