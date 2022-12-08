from itertools import chain

class Directory:
    def __init__(self, dirname, parent):
        self.dirname = dirname
        self.parent = parent
        self.files = {}
        self.directories = {}
        self.calculated_size = 0

        
    def add_directory(self, dirname):
        self.directories[dirname] = Directory(dirname, self)

        
    def add_file(self, filename, size):
        self.files[filename] = size

        
    def get_directory(self, dirname):
        return self.directories[dirname]

    
    def calculate_size(self):
        self.calculated_size = sum(self.files.values())
        self.calculated_size += sum(map(lambda x: x.calculate_size(), self.directories.values()))
        return self.calculated_size

    
    def get_directories_sizes(self):
        return list([self.calculated_size] + list(chain(*list(map(lambda x: x.get_directories_sizes(),
                                                                  self.directories.values())))))
    


def cd(command: str, i, current_dir: Directory):
    directory = command.split(" ")[-1]
    if directory == "/":
        current_dir = root_dir
    elif directory == "..":
        current_dir = current_dir.parent
    else:
        current_dir = current_dir.get_directory(directory)
    i += 1
    return i, current_dir

    
def ls(i, current_dir):
    i += 1
    while i < len(input_file):
        if input_file[i].startswith("$"):
            break
        elif input_file[i].startswith("dir"):
            dirname = input_file[i].split(" ")[1]
            current_dir.add_directory(dirname)
        else: #file
            content = input_file[i].split(" ")
            size = int(content[0])
            filename = content[1]
            current_dir.add_file(filename, size)
        i += 1
    return i, current_dir


def main():
    i: int = 0    
    current_dir: Directory = root_dir

    
    while i < len(input_file):
        a = input_file[i]
        if a.startswith("$ cd"):
            i, current_dir = cd(a, i, current_dir)
        elif a.startswith("$ ls"):        
            i, current_dir = ls(i, current_dir)

        
    root_dir.calculate_size()
    sizes = root_dir.get_directories_sizes()
    print("Part 1:\t", sum(filter(lambda x: x <= 100000, sizes)))
    
    disk_space = 70000000
    used = root_dir.calculated_size
    unused = disk_space - used
    needed = 30000000
    print("Part 2:\t", min(filter(lambda x: unused + x >= needed, sizes)))

    
root_dir = Directory("/", None)
input_file = list(filter(lambda x: x != "", open("7.txt", "r").read().split("\n")))
main()        
