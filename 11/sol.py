from itertools import *
from collections import *
from heapq import *
from copy import deepcopy, copy
from functools import *

with open(0) as file:
    data = file.read().rstrip().split()
    stones = [int(x) for x in data]

print(stones)

def step(stone : int):
    new = []
    if stone == 0:
        new.append(1)
    elif len(str(stone)) % 2 == 0:
        L = len(str(stone))
        left, right = str(stone)[:L // 2], str(stone)[L // 2:]
        new.append(int(left))
        new.append(int(right))
    else:
        new.append(stone * 2024)
    return new 

@cache
def step_steps(stone : int, i : int):
    if i == 0:
        return 1
    if stone == 0:
        return step_steps(1, i-1)
    elif len(str(stone)) % 2 == 0:
        L = len(str(stone))
        left, right = str(stone)[:L // 2], str(stone)[L // 2:]
        return step_steps(int(left), i-1) + step_steps(int(right), i-1)
    else:
        return step_steps(2024*stone, i-1)


new = stones
for _ in range(25):
    current = copy(new)
    new = []
    for i, stone in enumerate(current):
        new += step(stone)
    
p1 = len(new)
# Part 1
print(f"Part 1: {p1}")

p2 = sum([step_steps(stone, 75) for stone in stones])
# Part 2
print(f"Part 2: {p2}")

