import os

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

data = file.read().splitlines()

def f_path_calc():

    f_path = []
    f_sizes = {}

    for line in data:
        cmd = line.split()
        if cmd[0] == "$":
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    f_path = f_path[:-1]
                elif cmd[2] == "/":
                    f_path = ["/"]
                else:
                    f_path.append(cmd[2])
        else:
            if cmd[0] != "dir":
                curr_path = ""
                for folder in f_path:
                    if curr_path != "/" and folder != "/":
                        curr_path += "/"
                    curr_path += folder
                    f_sizes[curr_path] = f_sizes.get(curr_path, 0) + int(cmd[0])

    sum = 0
    for val in f_sizes.items():
        size = val[1]
        if size < 100000:
            sum += size
    # part 2

    vals = []
    for val in f_sizes.items():
        size = val[1]
        space = 30000000 - (70000000 - f_sizes.get("/"))
        if size >= space:
            vals.append(size)

    return min(vals)

# sum(value for name, value in f_sizesitems() if value < 100000)
print(f_path_calc())
