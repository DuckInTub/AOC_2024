obstacles = set()
with open(0) as file:
    data = file.read().rstrip().splitlines()
    HEIGHT, WIDTH = len(data), len(data)
    for y, row in enumerate(data):
        for x, elem in enumerate(row):
            if elem == "#":
                obstacles.add((x, y))
            elif elem == "^":
                start = (x, y)

def turn(facing):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return dirs[(dirs.index(facing)+1) % 4]

def simulate(start, obstacles):
    been = set()
    at = start
    facing = (0, -1)
    been.add((start, facing))
    while True:
        x, y = at
        dx, dy = facing
        new = x+dx, y+dy
        while new in obstacles:
            facing = turn(facing)
            dx, dy = facing
            new = x+dx, y+dy
        if not (0 <= new[0] < WIDTH and 0 <= new[1] < HEIGHT):
            return set(X for X, _ in been)
        if (new, facing) in been:
            return False
        been.add((new, facing))
        at = new

been = simulate(start, obstacles)
p1 = len(been)
# Part 1
print(f"Part 1: {p1}")

p2 = 0
for pos in been:
    if pos in obstacles or pos == start:
        continue
    new_obstacles = obstacles.union([pos])
    assert len(new_obstacles) > len(obstacles)
    if not simulate(start, new_obstacles):
        p2 += 1
        x, y = pos
        # print(y+1, x+1)

# Part 2
print(f"Part 2: {p2}")

