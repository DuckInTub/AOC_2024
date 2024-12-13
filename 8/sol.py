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
            
p1 = 0
antis1 = set()
antis2 = set()
for symbol, locations in antennas.items():
    for ant1, ant2 in combinations(locations, 2):
        r1, c1 = ant1
        r2, c2 = ant2
        dr, dc = r1 - r2, c1 - c2

        anti1 = r2 - dr, c2 - dc
        anti2 = r1 + dr, c1 + dc

        for x, y in [anti1, anti2]:
            if x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
                antis1.add((x, y))


        for i in range(50):
            anti1 = r2 - i*dr, c2 - i*dc
            anti2 = r1 + i*dr, c1 + i*dc

            for x, y in [anti1, anti2]:
                if x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
                    antis2.add((x, y))

# Part 1
print(f"Part 1: {len(antis1)}")

# Part 2
print(f"Part 2: {len(antis2)}")

