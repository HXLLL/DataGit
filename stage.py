from typing import List
from modify import Modify
from directory import Directory
from transform import Transform
from update import Update
from storage import storage
from blob import Blob
from version import Version
from typing import Tuple
import os
import utils
import shutil

class Stage():
    def __init__(self):
        self.__modify_sequence: List[Modify] = []
        self.root_dir: str = storage.get_working_dir()  # 这需要storage比Stage先初始化
        self.dir_tree: Directory = None
        self.__sync_dir_tree(self.root_dir)

    def __scan_update(self, dir) -> Tuple[list, list]:
        '''
        功能:扫描dir文件夹里的修改。如果dir或dir的几层父目录之前不存在,那么也要放到Dir里面
        参数:dir是绝对路径
        返回值:返回改动的add_list和remove_list
            add_list的元素都是元组(path:str,file:Directory/Blob)
            remove_list的元素是path:str
            path是从工作区的根目录开始的
        '''

        '''
        dir文件夹在工作区内一定存在
        如果Dir的父文件夹不存在,要把dir的新增父文件夹的Dir构造出来
        '''
        assert(os.path.exists(dir))
        dir = os.path.relpath(dir, self.root_path)  # dir转为相对路径
        dir = os.path.normpath(dir)
        dirs = dir.split(os.sep)
        if dirs[0] == '.':
            del dirs[0]
        
        u = self.dir_tree
        path = '.'
        stop = -1
        for i, dirname in enumerate(dirs):
            v = u.enter(dirname)
            if not v:
                stop = i
                break
            u = v
            path = os.path.join(path, dirname)
        if stop == -1:
            '''
            dir在stage中存在
            '''
        elif stop == len(dirs) - 1:
            '''
            dir在stage中不存在,但dir的上一级目录在stage中存在
            '''
        else:
            '''
            dir和上面的某几级目录在stage中都不存在
            '''
            dirs = dirs[i:]
        # 没写完
        # 思路：对工作区里的dir构造新Directory覆盖旧的



    def update(self, dir: str) -> None:
        '''
        参数是绝对路径
        '''
        assert(utils.in_working_dir(dir))

        add_list, del_list = self.__scan_update(dir)
        upd = Update(add_list, del_list)
        self.__modify_sequence.append(upd)
    
    def add(self, src: str, dst: str) -> None:
        '''
        参数都是绝对路径
        '''

        '''
        1.检查dst是否重名,若重名则报错（暂时方案）
        2.建dst文件夹
        3.把src里面的东西扔到dst里面
        4.建立dst文件夹的Directory结构
        5.把dir结构扔到modify_sequence里面
        '''
        assert(utils.in_working_dir(dst))
        assert os.path.exists(src)
        assert not os.path.exists(dst)

        # 把src里的所有东西复制到dst
        for src_dir, dirnames, filenames in os.walk(src):
            print('a:', src_dir, dirnames, filenames)
            for filename in filenames:
                rel_dir = os.path.relpath(src_dir, src)
                dst_dir = os.path.join(dst, rel_dir)
                src_file = os.path.join(src_dir, filename)
                dst_file = os.path.join(dst_dir, filename)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                shutil.copy(src_file, dst_file)
        
        self.update(dst)

    
    def transform(self, dir1: str, entry: str, isMap: int, dir2: str, message: str):
        '''
        新建一个Transform实例,添加到modify_sequnece中,并应用到工作目录
        '''

        m = Transform(isMap, dir1, entry, dir2, message)
        self.__modify_sequence.append(m)

        m.apply(storage.get_working_dir())
    
    def commit(self,parentID: int, id: int, message: str) -> Version:
        '''
        新建并返回一个Version实例
        '''
        new_version = Version(parentID, id, self.__modify_sequence, message)
        return new_version

    def status(self):
        pass