# coding=utf-8
def cal_absolute_square(distance):
    result = []
    for i in range(1, distance+1):
        if distance % i == 0:
            j = distance/i
            m = (i+j)/2
            n = (i-j)/2
            if (m > 0) and (n > 0) and (m+n == i) and (m-n == j) and (m > n) and (m % 1 ==0) and(n % 1 == 0):
                result.append(n)
                print("现在m="+str(m)+"，n="+str(n))
    return result


num = cal_absolute_square(168)
print(num)
