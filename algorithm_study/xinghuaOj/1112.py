target = input().lower()
line = input().lower()
lenLine = len(line)
count = 0
pos = -1
lastSpace = 0
for i in range(0, lenLine):
    if (line[i] == " "):
        tempStr = line[lastSpace:i]
        if (tempStr == target):
            if (pos == -1):
                pos = i - len(tempStr)
            count += 1
        lastSpace = i + 1
    elif (i == lenLine - 1):
        tempStr = line[lastSpace:i + 1]
        if (tempStr == target):
            if (pos == -1):
                pos = i - len(tempStr)
            count += 1

if (pos == -1):
    print(pos)
else:
    print(count, pos)
