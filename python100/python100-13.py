from math import floor
for i in range(100, 1000):
    a = floor(i/100)
    b = floor((i-a*100)/10)
    c = floor(i - a * 100 - b * 10)
    if(a**3+b**3+c**3==i):
        print(i," ")