from itertools import *
from collections import *
from heapq import *


with open(0) as file:
    data = file.read().rstrip().splitlines()
    blocked = []
    for row in data:
        X, Y = row.split(",")
        blocked.append((int(Y), int(X)))

def simulate(start, end, blocked_positions):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    Q = deque()
    Q.append((0, start))
    seen = set()
    while Q:
        steps, at = Q.popleft()
        if at == end:
            return steps
        if at in seen:
            continue
        seen.add(at)

        for direction in dirs:
            r, c = at
            dr, dc = direction
            nr, nc = r+dr, c+dc
            if (nr, nc) not in blocked_positions and 0 <= nr <= end[0] and 0 <= nc <= end[1]:
                Q.append((steps+1, (nr, nc)))
    
    return False

num_p1_blocks = 1024
block_set = set(blocked[:num_p1_blocks])
assert len(block_set) == num_p1_blocks
p1 = simulate((0, 0), (70, 70), block_set)
# Part 1
print(f"Part 1: {p1}")

for num in reversed(range(len(blocked))):
    curr_block_set = set(blocked[:num])
    assert len(curr_block_set) == num
    if simulate((0, 0), (70, 70), curr_block_set):
        thing = blocked[num]
        p2 = f"{thing[1]},{thing[0]}"
        break

# Part 2
print(f"Part 2: {p2}")

