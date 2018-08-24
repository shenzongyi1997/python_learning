# coding=utf-8
from math import pow
def wei_shu(num):
    count = 0
    while num >= 1:
        num /= 10
        count += 1
    return count
def reverse_print(num):
    for i in range(0, wei_shu(num)):
        temp = int((num % pow(10, i + 1)) / pow(10, i))
        print(temp, end='')

num = int(input('输入你想倒序输出的数字:'))
print('这个数字是个', wei_shu(num), '位数', sep='')
reverse_print(num)