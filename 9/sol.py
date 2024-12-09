from itertools import *
from collections import *
from heapq import *

with open(0) as file:
    data = file.read().rstrip()
    file_system = []
    disk_layout = []
    id_ = 0
    idx = 0
    for i, num in enumerate(data):
        if int(num) == 0:
            continue
        if i % 2 == 0:
            file_system += [id_] * int(num)
            disk_layout.append((id_, int(num), idx))
            id_ += 1
        else:
            file_system += [None] * int(num)
            disk_layout.append((None, int(num), idx))
        idx += 1
    

rev = [x for x in file_system if x != None]
i = 0
p1 = 0
elem = file_system[i]
while elem != rev[-1]:
    elem = file_system[i]

    if elem != None:
        p1 += elem * i
    else:
        last = rev.pop()
        p1 += last*i

    i += 1

# Part 1
print(f"Part 1: {p1}")

p2 = 0
to_move = [file for file in disk_layout if file[0] != None]
for _, mover in enumerate(reversed(to_move)):
    movID, movLen, movIndx = mover
    for segment in disk_layout:
        segID, segLen, segIndx = segment
        if segID == None and segLen >= movLen:
            rest = disk_layout[segIndx+1:]
            disk_layout = disk_layout[:segIndx] + [(movID, movLen, segIndx)]
            if segLen-movLen > 0:
                disk_layout += [(None, segLen-movLen, segIndx+1)]
                disk_layout += [(x, y, z+1) for x, y, z in rest]
            else:
                disk_layout += [(x, y, z) for x, y, z in rest]

            for i, thing in list(enumerate(disk_layout))[::-1]:
                if thing[0] == movID:
                    break
            disk_layout[i] = (None, movLen, i)

            break


real_layout = []
for block in disk_layout:
    id_, length, indx = block
    real_layout += [id_] * length

p2 = 0
for i, elem in enumerate(real_layout):
    if elem == None:
        continue
    p2 += i*elem

# Part 2
print(f"Part 2: {p2}")

