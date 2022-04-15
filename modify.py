from abc import ABC, abstractmethod

class Modify(ABC):
    def __init__(self):
        self.description = "error: this should not be printed"
    
    @abstractmethod
    def apply(self):
        pass

    def apply(self, workingDir):
        pass
