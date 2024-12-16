from copy import deepcopy
from itertools import *
from collections import *
from heapq import *

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_CW(direction):
    return dirs[ (dirs.index(direction) + 1) % len(dirs)]

def turn_CC(direction):
    rev_dirs = list(reversed(dirs))
    return rev_dirs[ (rev_dirs.index(direction) + 1) % len(dirs)]

walls = set()
with open(0) as file:
    data = file.read().rstrip().splitlines()
    for r, row in enumerate(data):
        for c, elem in enumerate(row):
            if elem == "#":
                walls.add((r, c))
            if elem == "S":
                start = (r, c)
            if elem == "E":
                end = (r, c)

min_score = 1E10
facing = (0, 1)
seen = set()
Q = []
DIST = defaultdict(int)
Q.append((0, start, facing))
while Q:
    score, at, facing = heappop(Q)
    r, c = at
    dr, dc = facing
    if (at, facing) not in DIST:
        DIST[(at, facing)] = score
    if (at, facing) in seen:
        continue
    if at == end:
        min_score = min(min_score, score)
        continue
    seen.add((at, facing))
    nr, nc = r+dr, c+dc
    if (nr, nc) not in walls:
        heappush(Q, (score+1, (nr, nc), facing))
    heappush(Q, (score+1000, at, turn_CC(facing)))
    heappush(Q, (score+1000, at, turn_CW(facing)))

seen = set()
Q = [(0, end, D) for D in dirs]
heapify(Q)
part_of_best = set()
while Q:
    score, at, facing = heappop(Q)
    r, c = at
    dr, dc = facing
    if (at, facing) in seen:
        continue
    seen.add((at, facing))
    rev_dir = turn_CC(turn_CC(facing))
    if score + DIST[(at, rev_dir)] == min_score:
        part_of_best.add(at)
    if at == start:
        continue
    nr, nc = r+dr, c+dc
    if (nr, nc) not in walls:
        heappush(Q, (score+1, (nr, nc), facing))
    heappush(Q, (score+1000, at, turn_CC(facing)))
    heappush(Q, (score+1000, at, turn_CW(facing)))

# Part 1
print(f"Part 1: {min_score}")
# Part 2
print(f"Part 2: {len(part_of_best)}")

