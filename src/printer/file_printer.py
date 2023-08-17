
def print_children(node):
    if node.type != "dir":
        return 0
    print("Director Listenings")
    total = 0
    for i in node.children:
        filename = i.name if i.type == "file" else i.name+"/"
        print("\t - %s" % filename)
        total += 1
    print("total entries - %d" % total)