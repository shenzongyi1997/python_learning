a = 1


def allNum( n ):
    if n <= 2:
        return 1
    else:
        return allNum(n-1)+allNum(n-2)


def allNum2( n ):
    if n <= 2:
        return 1
    else:
        num = [1, 1]
        for i in range(2, n):
            num.append(num[i-1]+num[i-2])
        return num[n-1]


print(allNum(10))
print(allNum2(10))