# coding=utf-8
from math import floor, pow
def wei_shu(num):
    count = 0
    while num >= 1:
        num /= 10
        count += 1
    return count
def is_hui_wen_shu(num):
    length = wei_shu(num)
    for i in range(0, floor(length / 2)):
        re_i = length - i - 1
        v_in_i = int(num % pow(10, i + 1) / pow(10, i))
        v_in_re_i = int(num % pow(10, re_i + 1) / pow(10, re_i))
        #print(v_in_i, '  ', v_in_re_i)
        if v_in_i != v_in_re_i:
            return False
    return True

num = int(input('请输入数字：'))
if is_hui_wen_shu(num):
    print(num, '是回文数', sep='')
else:
    print(num, '不是回文数', sep='')