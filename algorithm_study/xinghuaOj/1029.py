a, b = map(int, input().split())
count = 0
for i in range(a, b + 1):
    tmp = str(i)
    for s in tmp:
        if s == '2':
            count += 1
print(count)
