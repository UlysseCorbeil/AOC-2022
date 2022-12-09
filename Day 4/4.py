import os

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

data = file.read().splitlines()

def get_range(r):
    n = tuple(int(c) for c in r.split("-"))
    return range(n[0], n[1] + 1)

def subset(x, y):
    return not(False in [z in y for z in x])

sub_pairs = 0
overlaps = 0

for line in data:
    _a_r, _b_r = line.split(",")
    a, b = get_range(_a_r), get_range(_b_r)

    if subset(a, b) or subset(b, a):
        sub_pairs += 1

    if set(a).intersection(set(b)) != set():
        overlaps += 1

print(sub_pairs)
print(overlaps)
