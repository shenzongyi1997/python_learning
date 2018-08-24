def output(s, l):
    if l < 0:
        return
    else:
        print(s[l - 1], end='')
        output(s, l - 1)

st = 'abcde'
output(st, 5)