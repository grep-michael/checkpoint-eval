

class CommandHandler():

    def __init__(self,current_node) -> None:
        self.manual_commands = ["cd"]
        self.current_node = current_node

    def handle_command(self,current_node,cmd):
        self.current_node = current_node
        cmd = cmd.split(" ")
        command = cmd[0]
        args = " ".join(cmd[1:])

        if not command in self.manual_commands:
            self.__node_command__(command,args)

        self.__manual_command__(command,args)

        return self.current_node

    def __node_command__(self,command,args):
        if hasattr(self.current_node, command):
            func = getattr(self.current_node,command)
            func(args)
    
    def __manual_command__(self,command,args):
        if command == "cd":
            child_node = self.current_node.check_directory(args)
            if child_node != None:
                print("{} -> {}".format(self.current_node.name, child_node.name))
                self.current_node = child_node
            elif args == ".." and self.current_node.parent != None:
                print("{} <- {}".format(self.current_node.parent.name, self.current_node.name))
                self.current_node = self.current_node.parent
