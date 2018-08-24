from math import floor
n = int(11)
for i in range(0, floor(n / 2) + 1):
    for j in range(0, floor(n / 2) - i):
        print(' ', end='')
    for j in range(0, i * 2 - 1):
        print('*', end='')
    print()
for i in range(floor(n / 2) + 1, n):
    for j in range(0, i - floor(n / 2)):
        print(' ', end='')
    if n % 2 == 0:
        for j in range(0, (floor(n) - i) * 2 - 1):
            print('*', end='')
    else:
        for j in range(0, (floor(n) - i - 1) * 2 - 1):
            print('*', end='')
    print()