n = int(input())
total = []
for it in range(1, n + 1):
    temp = list(map(int, input().split()))
    sum = temp[0] + temp[1] + temp[2]
    total.append([it, sum, temp[0]])

total.sort(key=lambda x: (-x[1], -x[2], x[0]))
for i in range(0, 5):
    print(total[i][0], total[i][1])
