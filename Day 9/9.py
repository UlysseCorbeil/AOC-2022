import os
import numpy as np

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

data = file.read().splitlines()
dirs = {
    "R" : [1, 0],
    "L" : [-1, 0],
    "U" : [0, 1],
    "D" : [0, -1],
}

def f_rope_vis(k):
    rope = np.zeros((k+1, 2))
    tails = set()
    # base case
    tails.add((0, 0))

    for move in data:
        direction, ind = move.split()

        for _ in range(int(ind)):
            rope[0] += dirs[direction]
            for n in range(len(rope) - 1):
                # print(rope)
                t_dif = rope[n] - rope[n + 1]
                if np.any(abs(t_dif) > 1):
                    rope[n+1] += np.clip(t_dif, -1, 1)
                if n == len(rope) - 2:
                    tails.add((rope[n + 1][0], rope[n + 1][1]))
    return len(tails)

print(f_rope_vis(9))
