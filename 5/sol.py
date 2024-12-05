from itertools import *
from collections import *
from heapq import *
from functools import *

with open(0) as file:
    rules, updates = file.read().rstrip().split("\n\n")
    rules = [rule.split("|") for rule in rules.splitlines()]
    rules = [(int(L), int(R)) for L, R in rules]
    updates = [update.split(",") for update in updates.splitlines()]
    updates = [[int(x) for x in update] for update in updates]

def follows_rule(update, rule):
    L, R = rule
    try:
        return update.index(L) < update.index(R)
    except ValueError:
        return True

def compare(x, y):
    for L, R in rules:
        if L == x and R == y:
            return -1
        if L == y and R == x:
            return 1
    return 0


p1 = 0
p2 = 0
for update in updates:
    if all(follows_rule(update, rule) for rule in rules):
        mid = update[len(update)//2]
        p1 += mid
    else:
        update = sorted(update, key=cmp_to_key(compare))
        mid = update[len(update)//2]
        p2 += mid


# Part 1
print(f"Part 1: {p1}")
# Part 2
print(f"Part 2: {p2}")

