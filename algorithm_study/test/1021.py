import math
from math import sqrt


def isPrime(n):
    '''
    质数判断
    '''
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    stop = int(math.sqrt(n))
    for i in range(2, stop + 1):
        if (n % i == 0):
            return False
    return True


max = 0
min = 65336
iarr = list(map(str, input().strip()))  #切割
for i in set(iarr):
    if (iarr.count(i) > max):
        max = iarr.count(i)
    if (iarr.count(i) < min):
        min = iarr.count(i)
if (isPrime(max - min)):
    print("Lucky Word")
    print(max - min)
else:
    print("No Answer")
    print(0)
