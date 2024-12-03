from itertools import *
from collections import *
from heapq import *
import re

with open(0) as file:
    data = file.read().rstrip()
    finds = re.findall("mul\(\d+,\d+\)", data)

p1 = 0
for find in finds:
    L, R = re.findall("\d+", find)
    p1 += int(L) * int(R)
print(finds)

# Part 1
print(f"Part 1: {p1}")
# Part 2
print(f"Part 2: {p2}")

