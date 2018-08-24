year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))
dayMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0
for i in range(1, month):
    result += dayMonth[i]
result += day
if ((year % 400 == 0) or ((year % 100 !=0) and (year % 4 == 0))) and(month > 2):
    result +=1
print("today is the ", result, " day")
