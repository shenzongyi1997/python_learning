import math
def is_prime( num ):
    for i in range(2,math.floor(math.sqrt(num))+2):
        if num % i == 0:
            return False
    return True

def prime_number(start , end):
    for i in range(start,end+1):
        if is_prime(i):
            print(i, " ")

start = int(input("please input the start:"))
end = int(input("please input the end:"))
prime_number(start, end)