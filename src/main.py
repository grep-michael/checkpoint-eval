
from filestruct.file_structure import *

TEST = True


def main():
    root = Directory("root")
    if TEST:
        test_fill(root)    
    current_node = root
    print("""
Flawless Files v1.0
""")
    while 1:
        cmd = input(">")
        current_node = run_cmd(current_node,cmd)

def run_cmd(current_node, cmd):
    cmd = cmd.split(" ")
    command = cmd[0]
    args = " ".join(cmd[1:])
    if hasattr(current_node, command):
        func = getattr(current_node,command)
        func(args)
    
    if command == "cd":
        child_node = current_node.check_directory(args)
        if child_node != None:
            print("{} -> {}".format(current_node.name, child_node.name))
            current_node = child_node
        elif args == ".." and current_node.parent != None:
            print("{} <- {}".format(current_node.parent.name, current_node.name))
            current_node = current_node.parent
    return current_node

def test_fill(r):
    docs = Directory("Documents")
    r.__append_child__(docs)
    docs.touch("My work")
    docs.touch("taxes")

if __name__ == "__main__":
    main()