from modify import Modify

class Update(Modify):
    def __init__(self, add_list: list, remove_list: list):
        '''
        两个list的元素都是元组(path:str,file:Directory/Blob)
        path是从工作区的根目录开始的
        '''
        super().__init__()
        self.__add_list = add_list
        self.__remove_list = remove_list
    
    def apply(self):
        pass
