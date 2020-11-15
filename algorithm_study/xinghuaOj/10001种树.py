"""
9
4 
1 4 2 
4 6 1 
8 9 2 
3 5 2 


[1, 4, 2, 0]
[3, 5, 2, 0]
[4, 6, 1, 0]
[8, 9, 2, 0]
"""
treeNums = int(input())
hopeNums = int(input())
targetList = []

for i in range(hopeNums):
    targetList.append(list(map(int, input().split())))
targetList.sort(key=lambda x: (x[1]))  #从小到大排
roadList = [False for n in range(0, targetList[hopeNums - 1][1] + 1)]  #路段似乎得建大点 因为遍历的时候没0点
treeCount = 0
for it in targetList:
    print(it)
    if (it[2] > 0):  #需要目标还没完成 就继续种树
        count = 0
        for j in roadList[it[0]:it[1]]:
            """
           遍历区间 看看还需要种多少树
            """
            # print("target:", it[2], roadList[j], "count:", count)
            if (roadList[j]):  # 如果检测到种树ss
                count += 1

            for j in range(it[1], it[0] - 1, -1):
                if (count < it[2]) and (roadList[j] == False):
                    """
                    倒着遍历每个区间 如果已经种的树比需要种的少 
                    且 如果标记为没种树 
                    """
                    #  print("j:", j, "left:", it[0], "right:", it[1], roadList[j])
                    """
                    如果
                    """
                    roadList[j] = True  #标记已种树
                    print("在 roadlist", j, "位置种树")
                    it[2] -= 1  #目标值-=1
                    treeCount += 1

for it in targetList:
    print(it)
print(treeCount)
