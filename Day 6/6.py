import os

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

data = file.read().splitlines()[0]

def f_chars_pack(n):
    for k in range(len(data[n - 1:])):
        _c = set(data[k:k + n])
        if n == len(_c):
            return k + n
print(f_chars_pack(4))
print(f_chars_pack(14))
