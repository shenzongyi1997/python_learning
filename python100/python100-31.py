# coding=utf-8
def judge(week, idx):
    satisfy = []
    st = '请输入第' + str(idx + 1) + '个字母:'
    temp = input(st)
    for i in week:
        if i[idx] == temp:
            satisfy.append(i)
    if len(satisfy) == 1:
        print(satisfy[0])
    elif len(satisfy) == 0:
        print("没有符合要求的答案！")
    else:
        judge(satisfy, idx + 1)


week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
judge(week, 0)

