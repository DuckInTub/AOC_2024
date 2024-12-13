from itertools import *
from collections import *
from heapq import *
import re

with open(0) as file:
    data = file.read().rstrip().split("\n\n")
    problems = []
    for group in data:
        G = []
        for line in group.splitlines():
            x, y = re.findall(r"\d+", line)
            x, y = int(x), int(y)
            G.append((x, y))
        problems.append(G)

def is_whole_number(num : float, tolerance=0.01):
    return abs(num - round(num)) < tolerance

p1 = 0
for problem in problems:
    aButton, bButton, goal = problem
    ax, ay = aButton
    bx, by = bButton
    X, Y = goal
    # i*ax+j*bx=X, i*ay+j*by=Y
    nr_press_B = (Y - X*ay/ax) / (by - bx*ay/ax)
    nr_press_A = (X - nr_press_B*bx) / ax
    if all(is_whole_number(num) for num in [nr_press_A, nr_press_B]):
        nr_press_A, nr_press_B = round(nr_press_A), round(nr_press_B)
    else:
        continue
    assert nr_press_A*ax + nr_press_B*bx == X, f"{nr_press_A} and {nr_press_B}"
    assert nr_press_A*ay + nr_press_B*by == Y
    assert nr_press_A <= 100 and nr_press_B <= 100
    p1 += 3*nr_press_A + 1*nr_press_B


# Part 1
print(f"Part 1: {p1}")

p2 = 0
p2_dist = 10000000000000
for problem in problems:
    aButton, bButton, goal = problem
    ax, ay = aButton
    bx, by = bButton
    X, Y = goal[0]+p2_dist, goal[1]+p2_dist
    # i*ax+j*bx=X, i*ay+j*by=Y : Where i is nr_press_A and j is nr_press_B
    nr_press_B = (Y - X*ay/ax) / (by - bx*ay/ax)
    nr_press_A = (X - nr_press_B*bx) / ax
    if all(is_whole_number(num) for num in [nr_press_A, nr_press_B]):
        nr_press_A, nr_press_B = round(nr_press_A), round(nr_press_B)
    else:
        continue
    assert nr_press_A*ax + nr_press_B*bx == X, f"{nr_press_A} and {nr_press_B}"
    assert nr_press_A*ay + nr_press_B*by == Y
    p2 += 3*nr_press_A + 1*nr_press_B


# Part 2
print(f"Part 2: {p2}")

