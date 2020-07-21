year = int(input('请输入年份:'))

if year % 4 == 0:
    print(year, " 是闰年")
else:
    print(year, " 是平年")
