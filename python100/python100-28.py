# coding=utf-8
def age(n):
    if n == 1:
        return 10
    else:
        return 2 + age(n - 1)
num = int(input("请输入你想看第几个人的年龄:"))
print(age(num))

