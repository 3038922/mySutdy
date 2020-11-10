n = int(input())
total = 2

while (n > 1):
    if (total % 2 == 0):
        total += 1
    total *= 2
    n -= 1
print(total)