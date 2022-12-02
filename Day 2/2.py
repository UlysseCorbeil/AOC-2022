import os

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

data = file.read()
list_moves = []
for k in data.splitlines():
    list_moves.append(k.split(" "))

rnd_points = 0
for moves in list_moves:
    # for ind, _ in enumerate(moves):
    first = moves[0]
    last = moves[1]

    if first == "A":
        if last == "X":
            rnd_points += 3
            rnd_points += 0
        elif last == "Y":
            rnd_points += 1
            rnd_points += 3
        elif last == "Z":
            rnd_points += 2
            rnd_points += 6
    if first == "B":
        if last == "X":
            rnd_points += 1
            rnd_points += 0
        elif last == "Y":
            rnd_points += 2
            rnd_points += 3
        elif last == "Z":
            rnd_points += 3
            rnd_points += 6
    if first == "C":
        if last == "X":
            rnd_points += 2
            rnd_points += 0
        elif last == "Y":
            rnd_points += 3
            rnd_points += 3
        elif last == "Z":
            rnd_points += 1
            rnd_points += 6

print(rnd_points)
