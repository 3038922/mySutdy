isbn = input()
isbnlist = ''.join(isbn.split('-'))
total = 0
count = 0
while count < 9:
    total += int(isbnlist[count]) * (count + 1)
    count += 1

usercode = total % 11  # 识别码
if usercode == 10:  # 考虑余数为10，识别码为X的情况
    if isbnlist[9] == 'X':
        print('Right')
    else:
        print(isbn[0:12] + 'X')  # 对输入的字符串进行切片，取前12位
else:
    if isbnlist[9] == str(usercode):  # e为int型，要转化为str型
        print('Right')
    else:
        print(isbn[0:12] + str(usercode))
