from printer.file_printer import *


class FileNode():

    def __init__(self,name) -> None:
        self.children = []
        self.type = None
        self.parent = None
        self.name = name
    
    def ls(self,arg):
        print_children(self)
    
    def touch(self,name):
        if self.type != "dir":
            print("cant touch file")
            return 0
        self.__append_child__(File(name))

    def mkdir(self,name):
        if self.type != "dir":
            print("cant mkdir from file")
            return 0 
        self.__append_child__(Directory(name))

    def check_directory(self,directory_name):
        child = next((x for x in self.children if x.name == directory_name), None)
        return child
    
    def __append_child__(self,node):
        node.parent = self
        self.children.append(node)

class Directory(FileNode):
    
    def __init__(self,name) -> None:
        super().__init__(name)
        self.type = "dir"

class File(FileNode):

    def __init__(self,name) -> None:
        super().__init__(name)
        self.type = "file"