# coding=utf-8
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

i = 0
while i != -1:
    i = int(input("请输入n(想退出-1):"))
    if i != -1:
        print(fact(i))
