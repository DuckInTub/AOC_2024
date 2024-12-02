from itertools import *
from collections import *
from heapq import *

rows : list[list[int]] = []

with open(0) as file:
    data = file.read().rstrip().splitlines()
    for row in data:
        rows.append([int(num) for num in row.split()])

def increasing(row):
    return all(L < R for L, R in pairwise(row))

def decreasing(row):
    return all(L > R for L, R in pairwise(row))

def diffmax(row, diff):
    return all(abs(L - R) <= diff for L, R in pairwise(row))

def safe(testrow):
    return (increasing(testrow) or decreasing(testrow)) and diffmax(testrow, 3)
    
def part2safe(row):
    for i in range(len(row)):
        testrow = row[:i] + row[i+1:]
        if safe(testrow):
            return True
    return False


p1 = sum(safe(row) for row in rows)
p2 = sum(part2safe(row) for row in rows)

# Part 1
print(f"Part 1: {p1}")
# Part 2
print(f"Part 2: {p2}")

