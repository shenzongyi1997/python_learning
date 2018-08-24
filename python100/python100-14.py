import math
allPrime = []
def is_prime( num ):
    if num == 2:
        return True
    else:
        for i in range(2, math.floor(math.sqrt(num))+2):
            if num % i == 0:
                return False
        return True
def all_prime(n):
    for i in range(2, n+1):
        if is_prime(i):
            while n % i == 0:
                n = n / i
                allPrime.append(i)

num = int(input("please input the num:"))
all_prime(num)
for i in allPrime[0:len(allPrime)-1]:
    print( i , end='*')
print(allPrime[-1])
