money, total = map(int, map(int, input().split()))

for i in range(0, total // 5 + 1):
    for j in range(0, total // 3 + 1 - i):
        for z in range(0, total + 1 - i - j, 3):
            if (i * 5 + j * 3 + z // 3 == money and i + j + z == total):
                print(i, j, z)
