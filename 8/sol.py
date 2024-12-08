from itertools import *
from collections import *
from heapq import *

with open(0) as file:
    data = file.read().rstrip().splitlines()
    antennas = defaultdict(list)
    WIDTH, HEIGHT = len(data), len(data)
    for r, row in enumerate(data):
        for c, elem in enumerate(row):
            if elem == ".":
                continue
            antennas[elem].append((r, c))

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2) ** (1 / 2)

p1 = 0
antis = set()
for symbol, locations in antennas.items():
    for ant1, ant2 in combinations(locations, 2):
        r1, c1 = ant1
        r2, c2 = ant2
        dr, dc = r1 - r2, c1 - c2

        anti1 = r2 - dr, c2 - dc
        anti2 = r1 + dr, c1 + dc

        # print([ant1, ant2, anti1, anti2])

        x, y = anti1
        if x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
            antis.add(anti1)

        x, y = anti2
        if x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
            antis.add(anti2)

# Part 1
print(f"Part 1: {len(antis)}")

p2 = 0
antis = set()
for symbol, locations in antennas.items():
    for ant1, ant2 in combinations(locations, 2):
        r1, c1 = ant1
        r2, c2 = ant2
        dr, dc = r1 - r2, c1 - c2

        for i in range(50):
            anti1 = r2 - i*dr, c2 - i*dc
            anti2 = r1 + i*dr, c1 + i*dc

            x, y = anti1
            if x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
                antis.add(anti1)

            x, y = anti2
            if x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
                antis.add(anti2)


# Part 2
print(f"Part 2: {len(antis)}")

