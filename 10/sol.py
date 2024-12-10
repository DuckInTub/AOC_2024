from itertools import *
from collections import *
from heapq import *

with open(0) as file:
    data = file.read().rstrip().splitlines()
    elevations = defaultdict(int)
    starts = []
    WIDTH, HEIGHT = len(data[0]), len(data)
    for r, row in enumerate(data):
        for c, elem in enumerate(row):
            elevations[(r, c)] = int(elem)
            if elem == "0":
                starts.append((r, c))

def up_down_left_right(x, y):
    yield (x, y-1)
    yield (x, y+1)
    yield (x-1, y)
    yield (x+1, y)


p1 = 0
for start in starts:
    seen = set()
    next_step = deque()
    next_step.append(start)
    this_score = 0
    while next_step:
        at = next_step.popleft()
        if at in seen:
            continue
        if elevations[at] == 9:
            this_score += 1
            seen.add(at)
            continue
        seen.add(at)
        x, y = at

        for dx, dy in up_down_left_right(0, 0):
            new = x+dx, y+dy
            if new in seen:
                continue
            if elevations[new] != 1 + elevations[at]:
                continue
            if new[0] < 0 or new[1] < 0 or new[0] >= WIDTH or new[0] >= HEIGHT:
                continue

            assert elevations[new] == elevations[at] + 1
            next_step.append(new)

    p1 += this_score

# Part 1
print(f"Part 1: {p1}")

p2 = 0
for start in starts:
    next_step = deque()
    next_step.append(start)
    this_score = 0
    while next_step:
        at = next_step.popleft()
        x, y = at
        if elevations[at] == 9:
            this_score += 1
            continue

        for dx, dy in up_down_left_right(0, 0):
            new = x+dx, y+dy
            if elevations[new] != 1 + elevations[at]:
                continue
            if new[0] < 0 or new[1] < 0 or new[0] >= WIDTH or new[0] >= HEIGHT:
                continue

            assert elevations[new] == elevations[at] + 1
            next_step.append(new)

    p2 += this_score


# Part 2
print(f"Part 2: {p2}")

