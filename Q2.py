# coding=utf-8
# 为了解决在电梯上选钻石的问题，特意写的一个程序
import xlwt
import xlrd
import math
COUNT = 0
def my_find(seq):
    first = seq[0]
    result = 0
    for i in seq[1: len(seq)]:
        if i > first:
            if i == max(seq):
                result = 1
            break
    #print('seq = ', seq)
    #print('result = ', result)
    return result
def cal_chance(num):
    diamonds = list(range(1, num + 1))
    solve(num, diamonds)
def swap(a, b, seq):
    #print('a = ', a, "b = ", b)
    temp = seq[a]
    seq[a] = seq[b]
    seq[b] = temp
    return seq
def solve(num, seq):
    global COUNT
    if num == 1:
        COUNT += my_find(seq)
    else:
        for i in range(num):
            swap(i, num - 1, seq)
            solve(num - 1, seq)
            swap(num - 1, i,seq)
f = xlwt.Workbook()#创建工作簿
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
for i in range(0, 11):
    cal_chance(i)
    print(COUNT)
    sheet1.write(0, i, i)    #write的第一个,第二个参数时坐标, 第三个是要写入的数据
    sheet1.write(1, i, COUNT)
    sheet1.write(2, i, math.factorial(i))
    sheet1.write(3, i, COUNT / math.factorial(i))
    COUNT = 0
f.save("2.xls")#保存文件
