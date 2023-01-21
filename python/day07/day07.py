commands = open("day07.txt").read().split("\n")

class Directory:
    def __init__(self, name):
        self.name = name
        self.content = []

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def pr_filesystem(f, deep):
    for i in f:
        print("  " * deep + "- ", end="")
        if isinstance(i, File):
            print(i.name, f"(file, size={i.size})")
        else:
            print(i.name, "(dir)")
            pr_filesystem(i.content, deep+1)

def build_filesystem(commands):
    pointer = []
    filesystem = Directory(name="/")
    c = 1
    while c < len(commands):
        args = commands[c].split(" ")
        current = filesystem
        for p in pointer:
            current = current.content[p]
        current = current.content

        if args[0] == "$":
            if args[1] == "cd":
                if args[2] == "..":
                    pointer.pop(-1)
                else:
                    dir = next(d for d in range(len(current)) if current[d].name == args[2] and isinstance(current[d], Directory))
                    pointer.append(dir)
            if args[1] == "ls":
                pass
        else:
            if args[0] == "dir":
                current.append(Directory(name=args[1]))
            if args[0].isdigit():
                current.append(File(name=args[1], size=args[0]))
        c += 1
    return filesystem

def find_sizes(current_dir):
    global at_most

    dir_size = 0
    for f in current_dir.content:
        if isinstance(f, File):
            dir_size += int(f.size)
        else:
            dir_size += find_sizes(f)
    at_most += dir_size if dir_size <= 100000 else 0
    return dir_size

def possible_delete(current_dir):
    dir_size = 0
    for f in current_dir.content:
        if isinstance(f, File):
            dir_size += int(f.size)
        else:
            dir_size += possible_delete(f)
    if (AVAILABLE - used_space) + dir_size >= NEEDED:
        can_delete.append(dir_size)
    return dir_size

explorer = build_filesystem(commands)

AVAILABLE = 70000000
NEEDED = 30000000

at_most = 0
used_space = find_sizes(explorer)
can_delete = []
possible_delete(explorer)

print(used_space)
print(min(can_delete))