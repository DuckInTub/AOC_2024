from itertools import *
from collections import *
from heapq import *

with open(0) as file:
    data = file.read().rstrip().splitlines()

colL = []
colR = []
for row in data:
    row = row.split(" ")
    colL.append(int(row[0]))
    colR.append(int(row[-1]))

assert len(colL) == len(colR)

p1 = sum(abs(L - R) for L, R in zip(sorted(colL), sorted(colR)))

C = Counter(colR)
p2 = sum(num * C[num] for num in colL)

# Part 1
print(f"Part 1: {p1}")
# Part 2
print(f"Part 2: {p2}")

