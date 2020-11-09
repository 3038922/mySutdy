target = input().lower()
line = list(input().strip().lower().split())
count = 0
pos = -1
i = 0
for it in line:
    if it == target:
        if (pos == -1):
            pos = i
        count += 1
    i += 1
if (pos == -1):
    print(pos)
else:
    print(count, pos)
