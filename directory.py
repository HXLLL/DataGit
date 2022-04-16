from blob import Blob

class Directory():
    def __init__(self) -> None:
        self.file_list = []  # 元素类型可能是Directory或Blob
        self.name = 'null'   # 文件夹名称（不是路径）
