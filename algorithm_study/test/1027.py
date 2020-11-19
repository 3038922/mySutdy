count = 1
n = int(input())
for i in range(1, n + 1):
    for j in range(0, i):
        print(count, end='')
        count += 1
        if (count > 9):
            count = 0
    print()
