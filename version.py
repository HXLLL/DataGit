from modify import Modify
from update import Update


class Version:
    def __init__(self):
        self.modify_sequence = []

    def add_update(self, dir: str) -> None:
        m = Update()
        self.modify_sequence.append(m)
