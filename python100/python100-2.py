#coding=utf-8
def calcProfit(I):
    totalI = [0, 100000, 200000, 400000, 600000, 1000000]
    totalI.reverse()
    #   print(totalI)
    tax = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
    tax.reverse()
    #   print(tax)
    all_tax = 0
    for i in range(0, 6):
        if I > totalI[i]:
            all_tax += (I-totalI[i])*tax[i]
            I = totalI[i]
    return all_tax


I = int(input("请输入总利润:"))
print('总共奖金为:', calcProfit(I))
