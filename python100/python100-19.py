import math
from functools import reduce
def all_div(num):
    div_seq = []
    for i in range(1, num):
        if num % i == 0:
            div_seq.append(i)
    return div_seq
def complete_numbers(start, end):
    all_complete_numbers = []
    for i in range(start, end+1):
        div_numbers = all_div(i)
        if reduce(lambda x,y : x + y, div_numbers) == i:
            all_complete_numbers.append(i)
    return all_complete_numbers


complete_numb = complete_numbers(2, 1000)
print(complete_numb)

