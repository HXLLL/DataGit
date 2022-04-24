from blob import Blob
from typing import List, Tuple, Union, Dict
import os
import utils

class Directory():
    def __init__(self, name: str = '') -> None:
        self.__name: str = name      # 文件夹名称（不是路径）
        self.__files: Dict[str, Blob] = {}
        self.__dirs: Dict[str, Directory] = {}
    
    def get_name(self) -> str:
        return self.__name
    
    def get_files(self) -> Dict[str, Blob]:
        return self.__files
    
    def get_dirs(self) -> Dict[str, 'Directory']:
        return self.__dirs
    
    def set_dir(self, dir: 'Directory') -> None:
        self.__dirs[dir.get_name()] = dir
    
    def set_file(self, file: Blob) -> None:
        self.__files[file.get_name()] = file

    def unfold(self, root_path: str) -> List[Tuple[str, Blob]]:
        '''
        功能：展开目录，返回一些元组(完整路径,对应的Blob)
        '''
        return [file.unfold(os.path.join(root_path, self.__name)) 
                for file in self.__files.values()]
    
    def enter(self, filename: str) -> Union['Directory', Blob, None]:
        '''
        功能:返回名字为filename的子目录或者子文件
        返回值:存在则返回Directory或Blob,不存在则返回None
        '''
        return self.__files[filename] if filename in self.__files.keys() else None
      
    def copy(self, new_dir: 'Directory'):
        '''
        功能:复制new_dir的信息到self。用于就地更新目录树的某个节点而不改变父子关系。
        '''
        # print('copy', self.__name, new_dir.get_name())
        assert(self.__name == new_dir.get_name())  # 如果名字变了，父亲就找不到self。
        self.__files = new_dir.get_files()
        self.__dirs = new_dir.get_dirs()
        
    def build_dict(self, working_dir: str) -> None:
        '''
        获取working_dir下的子目录信息, 构造self.__dirs与self.__files
        '''
        for item in os.listdir(working_dir):
            abs_path = os.path.join(working_dir, item)
            if os.path.isdir(abs_path):
                if item != '.datagit':
                    self.__dirs[item] = Directory(item)
            else:
                file = Blob(item)
                file.set_hash(utils.get_hash(os.path.join(working_dir, item)))
                self.__files[item] = file
    
    def construct(self, working_dir: str) -> None:
        '''
        获得working_dir作为根目录的目录结构
        '''
        _, self.__name = os.path.split(working_dir)
        self.build_dict(working_dir)
        for item in self.__dirs:
            self.__dirs[item].construct(os.path.join(working_dir, item))
    
    def get_update_list(self, old: 'Directory', relpath: str) -> Tuple[list, list]:
        '''
        功能:找出self相对old的add_list和remove_list。当前这两个目录的相对路径都是relpath。
        '''
        old_dirs = old.get_dirs()
        old_files = old.get_files()

        add_list = []
        remove_list = []

        for new_file in self.__files.values():
            filename = new_file.get_name()
            print('filename:', filename)
            if filename in old_files:
                old_file = old_files[filename]
                print('new hash:', new_file.get_hash())
                print('old hash:', old_file.get_hash())
                print('equal:', new_file.get_hash() == old_file.get_hash())
                if new_file.get_hash() != old_file.get_hash():
                    remove_list.append((relpath, old_file))
                    add_list.append((relpath, new_file))
            else:
                add_list.append((relpath, new_file))
        
        for old_file in old_files.values():
            filename = old_file.get_name()
            if filename not in self.__files:
                remove_list.append((relpath, old_file))
        
        for new_dir in self.__dirs.values():
            dirname = new_dir.get_name()
            if dirname in old_dirs:
                old_dir = old_dirs[dirname]
                sub_add_list, sub_remove_list = new_dir.get_update_list(old_dir, 
                                                    os.path.join(relpath, dirname))
                add_list += sub_add_list
                remove_list += sub_remove_list
            else:
                add_list.append((relpath, new_dir))
        
        for old_dir in old_dirs.values():
            dirname = old_dir.get_name()
            if dirname not in self.__dirs:
                remove_list.append((relpath, old_dir))
        
        return add_list, remove_list
