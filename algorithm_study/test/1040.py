isbn = input()
isbnlist = ''.join(isbn.split('-'))
total = 0
count = 0
while count < 9:
    total += int(isbnlist[count]) * (count + 1)
    count += 1
usrcode = str(total % 11)
if (usrcode == '10'):
    usrcode = 'X'

if (usrcode == isbnlist[9]):
    print("Right")
else:
    print(isbn[0:12] + usrcode)
