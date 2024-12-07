from itertools import *
from collections import *
from heapq import *

def cardinals(y, x, L):
    for dx, dy in product([1, -1, 0], repeat=2):
        if dx == dy == x == y:
            continue
        yield [(y, x)] + [(y+dx*i, x+dy*i) for i in range(1, L)]
    

with open(0) as file:
    data = file.read().rstrip().splitlines()

print(list(cardinals(0, 0, 4)))
assert len(list(cardinals(0, 0, 4))) == 8

p1 = 0
for y, row in enumerate(data):
    for x, elem in enumerate(row):
        if elem == "X":
            for cardinal in cardinals(y, x, 4):
                string = ""
                for y, x in cardinal:
                    if y < 0 or x < 0 or y >= len(data) or x >= len(data):
                        break
                    string += data[y][x]
                if string == 'XMAS':
                    p1 += 1

# Part 1
print(f"Part 1: {p1}")
# Part 2
print(f"Part 2: {p2}")

