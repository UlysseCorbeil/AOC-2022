import os

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

data = file.read()
list_moves = []

rnd_points = 0

p_1 = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,

    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,

    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

p_2 = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,

    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,

    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

for k in data.splitlines():
    # rnd_points += p_1[k]
    
    rnd_points += p_2[k]


print(rnd_points)
