def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def all_fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        seq = [1, 1]
        for i in range(2, n):
            seq.append(seq[i-2]+seq[i-1])
        return seq


print(fib(10))
print(all_fib(10))
