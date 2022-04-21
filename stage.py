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
        self.dir_tree: Directory = Directory()
        self.dir_tree.construct(self.root_dir)
    
    def __get_update_list(self, cur_path: str, old_tree: Directory, 
                          new_tree: Directory) -> Tuple[list, list]:
        '''
        功能:生成new_tree相比old_tree的add_list和remove_list
            这两个文件夹在相对目录cur_path中
        '''
        

    def __scan_update(self, dir: str) -> Tuple[list, list]:
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
        new_dir_tree = Directory()
        new_dir_tree.construct(dir)  # new_dir_tree是工作区内dir的目录树
        dir_relpath = os.path.relpath(dir, self.root_path)  # 转为相对路径
        dir_relpath = os.path.normpath(dir_relpath)  # 转为标准格式
        dirs = dir.split(os.sep)  # 路径拆分
        if dirs[0] == '.':
            del dirs[0]
        
        u = self.dir_tree
        u_fa = None
        cur_path = '.'
        stop = -1
        for i, dirname in enumerate(dirs):
            v = u.enter(dirname)
            if not v:
                stop = i
                break
            u_fa, u = u, v
            cur_path = os.path.join(cur_path, dirname)
        
        add_list = []
        remove_list = []
        if stop == -1:
            '''
            dir在stage中存在
            此时cur_path是到dir的相对路径
            u是self.dir_tree的子孙结点,是dir的目录树
            '''
            add_list, remove_list = self.__get_update_list(cur_path, u, new_dir_tree)
            u.copy(new_dir_tree)
        elif stop == len(dirs) - 1:
            '''
            dir在stage中不存在,但dir的上一级目录在stage中存在
            此时cur_path是到dir上一级目录的相对路径
            u是self.dir_tree的子孙结点,是dir的上一级目录的目录树
            '''
            u.files[new_dir_tree.name] = new_dir_tree
            add_list = [(cur_path, new_dir_tree)]
        else:
            '''
            dir和上面的某几级目录在stage中都不存在
            '''
            fa_dir_tree = Directory(dirs[stop])  # 最上层的原本不存在的目录的树结构
            v = fa_dir_tree
            for dirname in dirs[stop+1:-1]:
                w = Directory(dirname)
                v.files['dirname'] = w
                v = w
            # v现在是dir的上级目录的目录树
            v.files[new_dir_tree.name] = new_dir_tree
            add_list = [(cur_path, fa_dir_tree)]
        
        return add_list, remove_list



    def update(self, dir: str) -> None:
        '''
        参数是绝对路径
        '''
        assert(utils.in_working_dir(dir))

        add_list, del_list = self.__scan_update(dir)
        upd = Update(add_list, del_list)
        self.__modify_sequence.append(upd)
        # todo:还要更新工作区状态
    
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