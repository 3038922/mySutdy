import math
a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2.0
temp = p * (p - a) * (p - b) * (p - c)
if (temp > 0):
    s = round(math.sqrt(temp), 2)
    print('%.2f' % s)
else:
    print("Can't")
