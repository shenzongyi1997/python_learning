# coding=utf-8
result = 0
num = 1
for i in range(1, 21):
    result += num
    num *= (i + 1)
    print("num = ", num, " i = ", i, "result = ", result)
print(result)
