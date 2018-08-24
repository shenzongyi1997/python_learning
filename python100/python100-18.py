# -*- coding: UTF-8 -*-
from functools import reduce
Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for i in range(0,n):
    Tn += a
    a *= 10
    Sn.append(Tn)

Sn = reduce(lambda x, y: x + y, Sn)
print("计算和为：", Sn)
