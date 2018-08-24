# coding=utf-8
def count_peaches(n):
    peaches = 1
    for i in range(1, n):
        peaches += 1
        peaches *= 2
    return peaches

day = int(input("请输入第几天还剩下一个:"))
print(count_peaches(day))
