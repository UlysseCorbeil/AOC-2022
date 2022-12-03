import os
from string import ascii_letters

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

_data = file.read().splitlines()

lower = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}
upper = {
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

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
