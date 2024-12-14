from copy import deepcopy
from itertools import *
from collections import *
from heapq import *
from math import prod, comb
import re

with open(0) as file:
    data = file.read().rstrip().splitlines()
    bots = []
    for line in data:
        x, y, dx, dy = re.findall(r"(\d+|-\d+)", line)
        r, c, dr, dc = [int(e) for e in (y, x, dy, dx)]
        bots.append([r, c, dr, dc])
    
old_bots = deepcopy(bots)
HEIGHT, WIDTH = 103, 101

def border(r, c):
    return (r % HEIGHT), (c % WIDTH)

def avg_dist(bots):
    total = 0
    for b1, b2 in combinations(bots, 2):
        r1, c1, _, _ = b1
        r2, c2, _, _ = b2
        total += abs(r2 - r1) + abs(c2 - c1)

    return total / comb(len(bots), 2)

def stateify(bots):
    state = []
    for bot in bots:
        r, c, _, _ = bot
        state += [r, c]
    return ",".join(str(e) for e in state)

newbots = []
for i, bot in enumerate(bots):
    r, c, dr, dc = bot
    nr, nc = r+dr*100, c+dc*100
    nr, nc = border(nr, nc)
    newbots.append([nr, nc, dr, dc])

# quadrants:
# 0 1
# 2 3
quadrants = [0, 0, 0, 0]
MH = HEIGHT // 2
MW = WIDTH // 2
for bot in newbots:
    r, c, dr, dc = bot
    if r<MH and c<MW:
        quadrants[0] += 1
    if r<MH and c>MW:
        quadrants[1] += 1
    if r>MH and c<MW:
        quadrants[2] += 1
    if r>MH and c>MW:
        quadrants[3] += 1

p1 = prod(quadrants)
# Part 1
print(f"Part 1: {p1}")

avg_dists = []
looped = False
seen = set()
steps = 1
while not looped:
    for i, bot in enumerate(bots):
        r, c, dr, dc = bot
        nr, nc = r+dr, c+dc
        nr, nc = border(nr, nc)
        bots[i] = [nr, nc, dr, dc]
    
    state = stateify(bots)
    if state in seen:
        looped = True
        break
    seen.add(state)
    dist = avg_dist(bots)
    avg_dists.append((steps, dist))
    steps += 1

T = min(avg_dists, key=lambda x : x[1])[0]
for i, bot in enumerate(old_bots):
    r, c, dr, dc = bot
    nr, nc = r+dr*T, c+dc*T
    nr, nc = border(nr, nc)
    old_bots[i] = [nr, nc, dr, dc]

mp = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
for bot in old_bots:
    r, c, _, _ = bot
    mp[r][c] = "#"
for line in mp:
    print("".join(line))

# Part 2
print(f"Part 2: {T}")

