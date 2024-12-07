from itertools import *
from collections import *
from heapq import *

with open(0) as file:
    data = file.read().rstrip().splitlines()
    totals = []
    parts = []
    for line in data:
        L, R = line.split(":")
        totals.append(int(L))
        parts.append([int(num) for num in R.split()])

def operators_make_total(total, sequence):
    ret = (False, False)
    operators = [lambda x, y: x+y, lambda x, y: x*y, lambda x, y: int(str(x)+str(y))]
    for operator_sequence in product(operators, repeat=len(sequence)-1):
        operator_sequence = list(operator_sequence)
        opp = operator_sequence[0]
        prev = opp(sequence[0], sequence[1])

        assert len(operator_sequence[1:]) == len(sequence[2:])

        for opp, elem in zip(operator_sequence[1:], sequence[2:]):
            prev = opp(prev, elem)

        if prev == total:
            ret = (operators[2] not in operator_sequence, True)
            if ret == (True, True):
                return ret

    return ret

p1 = 0
p2 = 0
for total, sequence in zip(totals, parts):
    p1B, p2B = operators_make_total(total, sequence)
    p1 += total if p1B else 0
    p2 += total if p2B else 0

# Part 1
print(f"Part 1: {p1}")
# Part 2
print(f"Part 2: {p2}")

