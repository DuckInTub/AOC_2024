from copy import deepcopy
from itertools import *
from collections import *
from heapq import *
import os

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

borders = set()
boxes = set()
borders2 = set()
boxes2 = dict()
moves = []
with open(0) as file:
    data = file.read().rstrip().split("\n\n")
    for r, row in enumerate(data[0].splitlines()):
        for c, elem in enumerate(row):
            c2 = 2*c
            if elem == "#":
                borders.add((r, c))
                borders2.add((r, c2))
                borders2.add((r, c2+1))
            if elem == "O":
                boxes.add((r, c))
                boxes2[(r, c2)] = "["
                boxes2[(r, c2+1)] = "]"
            if elem == "@":
                robot = (r, c)
                robot2 = (r, c2)
    
    for elem in "".join(data[1].rstrip().split()):
        D = DIRS["^>v<".index(elem)]
        moves.append(D)
    

for move in moves:
    r, c = robot
    dr, dc = move
    nr, nc = r+dr, c+dc
    robot = (nr, nc)
    if (nr, nc) in borders:
        robot = (r, c)
        continue
    if (nr, nc) in boxes:
        Ir, Ic = nr, nc
        while True:
            Ir, Ic = Ir+dr, Ic+dc
            if (Ir, Ic) not in boxes and (Ir, Ic) not in borders:
                robot = (nr, nc)
                boxes.remove((nr, nc))
                boxes.add((Ir, Ic))
                break
            if (Ir, Ic) in borders:
                robot = (r, c)
                break


p1 = 0
for (br, bc) in boxes:
    score = br*100 + bc
    p1 += score

# Part 1
print(f"Part 1: {p1}")

def draw_p2():
    D = data[0].splitlines()
    mp = [["." for c in range(2*len(D[1]))] for r in range(len(D))]
    for r, row in enumerate(mp):
        for c, elem in enumerate(row):
            if (r, c) in boxes2:
                mp[r][c] = boxes2[(r, c)]
            if (r, c) in borders2:
                mp[r][c] = "#"
            if (r, c) == robot2:
                mp[r][c] = "@"

    for line in mp:
        print("".join(line))
    
    print()


for move in moves:
    r, c = robot2
    dr, dc = move
    nr, nc = r+dr, c+dc
    robot2 = (nr, nc)
    affected = set()
    if robot2 in borders2:
        robot2 = (r, c)
        continue
    if robot2 in boxes2:
        affected = set()
        Q = deque()
        Q.append((nr, nc))
        if move in [(1, 0), (-1, 0)]:
            if boxes2[(nr, nc)] == "[":
                Q.append((nr, nc+1))
            if boxes2[(nr, nc)] == "]":
                Q.append((nr, nc-1))
            assert len(Q) % 2 == 0
        while Q:
            ir, ic = Q.popleft()
            if (ir, ic) in borders2:
                robot2 = (r, c)
                affected = set()
                Q = deque()
                break
            if (ir, ic) not in boxes2:
                continue

            assert (ir, ic) in boxes2
            affected.add((ir, ic))
            if move in [(1, 0), (-1, 0)]:
                Q.append((ir+dr, ic+dc))
                if boxes2.get((ir+dr, ic+dc), 0) == "[":
                    Q.append((ir+dr, ic+1))
                if boxes2.get((ir+dr, ic+dc), 0) == "]":
                    Q.append((ir+dr, ic-1))
            else:
                assert move in [(0, 1), (0, -1)]
                Q.append((ir, ic+dc))
    
    assert len(affected) % 2 == 0, affected
    new = dict()
    new = {k:v for k, v in boxes2.items() if k not in affected}
    for br, bc in affected:
        box_sym = boxes2.pop((br, bc))
        new[(br+dr, bc+dc)] = box_sym
    boxes2 = deepcopy(new)

draw_p2()
p2 = 0
for (r, c), box_sym in boxes2.items():
    if box_sym == "[":
        p2 += r*100 + c
# Part 2
print(f"Part 2: {p2}")

