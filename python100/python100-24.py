# coding=utf-8
from functools import reduce
up = []
down = []
seq = []
for i in range(20):
    if i == 0:
        up.append(2)
        down.append(1)
    elif i == 1:
        up.append(3)
        down.append(2)
    else:
        up.append(up[i - 1] + up[i - 2])
        down.append(down[i - 1] + down[i - 2])
    seq.append(up[i]/down[i])
result = reduce(lambda x, y: x+y, seq)
print(result)
