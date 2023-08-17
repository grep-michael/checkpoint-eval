
from filestruct.file_structure import *
from command_handler import *
TEST = True


def main():
    root = Directory("root")
    if TEST:
        test_fill(root)    
    current_node = root
    cmd_handle = CommandHandler(current_node)
    print("""
Flawless Files v1.0
""")
    while 1:
        cmd = input(">")
        current_node = cmd_handle.handle_command(current_node,cmd)


def test_fill(r):
    docs = Directory("Documents")
    r.__append_child__(docs)
    docs.touch("My work")
    docs.touch("taxes")

if __name__ == "__main__":
    main()