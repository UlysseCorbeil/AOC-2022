import os

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

data = file.read()

_sum = 0
sums = [0, 0, 0, 0]
for k in data.splitlines():
    if k.strip():
        _sum += int(k.strip())
    else:
        sums[0] = _sum
        sums.sort()
        _sum = 0

print(sums[3])
print(sum(sums[1:]))
