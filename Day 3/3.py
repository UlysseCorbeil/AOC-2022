import os
from string import ascii_letters

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

_data = file.read().splitlines()

# part 1
def p_1(data):
    priority = 0
    for line in data:
        first = line[:len(line)//2]
        second = line[len(line)//2:]

        matching = (set(first) & set(second)).pop()

        priority += ascii_letters.index(matching) + 1
    return priority

#part 2
def p_2(data):
    priority = 0
    for item in range(0, len(data), 3):
        first, sec, inter = data[item : item + 3]
        same = (set(first) & set(sec) & set(inter)).pop()
        priority += ascii_letters.index(same) + 1
    return priority

print(p_2(_data))
