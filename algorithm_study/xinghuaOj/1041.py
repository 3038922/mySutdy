robot1 = list(map(str, input().strip()))
robot2 = list(map(str, input().strip()))
recoderList = []
for r1 in robot1:
    for r2 in robot2:
        if (r2 == r1):
            if r2 not in recoderList:
                recoderList.append(r1)

recoderList.sort()
nums = len(recoderList)
if (nums == 0):
    print("WuXiao", end="")
elif (nums == 1):
    print("ZhiHui")
    print(recoderList[0], end="")
else:
    print("XLuo")
    print(nums)
    for i in range(0, nums):
        if (i < nums - 1):
            print(recoderList[i], end="-")
        else:
            print(recoderList[i], end="")
