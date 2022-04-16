from modify import Modify

class Update(Modify):
    def __init__(self, add_list: list, remove_list: list):
        super().__init__()
        self.__add_list = add_list
        self.__remove_list = remove_list
    
    def apply(self):
        pass
