# coding=utf-8
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def solve_jump(n):
    distance = 100
    height = 100
    height /= 2
    for i in range(1, n):
        distance += 2 * height
        height /= 2
    return height, distance

[height, distance] = solve_jump(10)
print(distance, ' ', height)