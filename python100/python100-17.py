# coding=utf-8
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


def cal_by_index( txt ):
    numOfEng = 0
    numOfSpace = 0
    numOfNum = 0
    numOfOthers = 0
    for i in range(0, len(txt)):
        if ('a' < txt[i] < 'z') or ('A' < txt[i] < 'Z'):
            numOfEng += 1
        elif '0' < txt[i] < '9':
            numOfNum += 1
        elif txt[i] == ' ':
            numOfSpace += 1
        else:
            numOfOthers += 1
    return "英语字符有" + str(numOfEng) + "个\n" + "数字字符有" + str(numOfNum) + "个\n" + "空格字符有" + str(numOfSpace) + "个\n" + "其他字符有" + str(numOfOthers) + "个"


def cal_by_char( txt ):
    numOfEng = 0
    numOfSpace = 0
    numOfNum = 0
    numOfOthers = 0
    for i in txt:
        if ('a' < i < 'z') or ('A' < i < 'Z'):
            numOfEng += 1
        elif '0' < i < '9':
            numOfNum += 1
        elif i == ' ':
            numOfSpace += 1
        else:
            numOfOthers += 1
    return "英语字符有" + str(numOfEng) + "个\n" + "数字字符有" + str(numOfNum) + "个\n" + "空格字符有" + str(
                numOfSpace) + "个\n" + "其他字符有" + str(numOfOthers) + "个"


txt = input("请输入字符串:")
print(cal_by_index(txt))
print(cal_by_char(txt))