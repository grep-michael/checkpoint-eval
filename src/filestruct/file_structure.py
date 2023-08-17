
class FileNode():

    def __init__(self) -> None:
        self.children = []
        self.type = ""
        self.parent = None

class Directory(FileNode):
    
    def __init__(self) -> None:
        super().__init__()
        self.type = "dir"

class File(FileNode):
    def __init__(self) -> None:
        super().__init__()
        self.type = "file"