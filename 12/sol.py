from itertools import *
from collections import *
from heapq import *

with open(0) as file:
    data = file.read().rstrip().splitlines()

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_CW(direction):
    return dirs[ (dirs.index(direction) + 1) % len(dirs)]

def turn_CC(direction):
    rev_dirs = list(reversed(dirs))
    return rev_dirs[ (rev_dirs.index(direction) + 1) % len(dirs)]

p1 = 0
p2 = 0
seen = set()
for r in range(len(data)):
    for c in range(len(data[0])):
        if (r, c) in seen:
            continue
        Q = deque()
        Q.append((r, c))
        curr_char = data[r][c]
        perim = 0
        perimeter_points = defaultdict(set)
        area = 0
        part_of_this = set()
        while Q:
            at = Q.popleft()
            if at in seen:
                continue
            seen.add(at)
            area += 1
            part_of_this.add(at)

            for dr, dc in dirs:
                x, y = at
                nr, nc = x+dr, y+dc
                if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and data[nr][nc] == curr_char:
                    Q.append((nr, nc))
                else:
                    perim += 1
                    perimeter_points[(dr, dc)].add((nr, nc))

        sides = 0
        for dir, points in perimeter_points.items():
            dir1 = turn_CC(dir)
            dir2 = turn_CW(dir)

            seen_perim = set()
            for point in points:
                if point in seen_perim:
                    continue
                sides += 1
                seen_perim.add(point)
                at1 = point
                at2 = point
                dr1, dc1 = dir1
                dr2, dc2 = dir2
                while (at1 in points) or (at2 in points):
                    if at1 in points:
                        seen_perim.add(at1)
                        at1 = at1[0]+dr1, at1[1]+dc1
                    if at2 in points:
                        seen_perim.add(at2)
                        at2 = at2[0]+dr2, at2[1]+dc2

        print(curr_char, area, sides)
        p1 += area*perim
        p2 += area*sides


# Part 1
print(f"Part 1: {p1}")
# Part 2
print(f"Part 2: {p2}")

