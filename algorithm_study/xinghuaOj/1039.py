n = int(input())
cityNum = ["A", "B", "C", "D", "E", "F", "G", "R", "S", "T"]
count = n
for i in range(0, n):
    carNum = input()
    for it in cityNum:
        if carNum[0] == it:
            count -= 1
            break

print(count)