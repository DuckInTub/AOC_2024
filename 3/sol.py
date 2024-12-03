from itertools import *
from collections import *
from heapq import *
import re

with open(0) as file:
    data = file.read().rstrip()
    finds = re.findall("mul\(\d+,\d+\)", data)
    p2finds = re.findall("(do\(\)|mul\(\d+,\d+\)|don't\(\))", data)

p1 = 0
for find in finds:
    L, R = re.findall("\d+", find)
    p1 += int(L) * int(R)
print(finds)

p2 = 0
DO = True
for find in p2finds:
    if find == "do()":
        DO = True
    elif find == "don't()":
        DO = False
    elif DO:
        L, R = re.findall("\d+", find)
        p2 += int(L) * int(R)


# Part 1
print(f"Part 1: {p1}")
# Part 2
print(f"Part 2: {p2}")

