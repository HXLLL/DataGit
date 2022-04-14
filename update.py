from modify import Modify

class Update(Modify):
    def __init__(self):
        super().__init__()
        self.description = "this is an update"
    
    def apply(self):
        print(self.description)