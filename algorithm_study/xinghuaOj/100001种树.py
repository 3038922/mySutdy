"""
9
4
1 4 2
4 6 2
8 9 2
3 5 2 

[8, 9, 2]
[4, 6, 2]
[3, 5, 2]
[1, 4, 2]
"""
treeNums = int(input())
hopeNums = int(input())
targetList = []
for i in range(hopeNums):
    targetList.append(list(map(int, input().split())))
    targetList[i].append(False)
targetList.sort(key=lambda x: (-x[1], -x[2]))

treeCount = 0
for i in range(hopeNums):
    if (targetList[i][3] == False):
        if (targetList[i][0] <= targetList[i + 1][1]):  #如果本次的端点和下次端点相交
            targetList[i][3] = True  #标注为已经种树
            treeCount += 1
            print(i, "相交或者相切", treeCount)
        else:
            targetList[i][3] = True  #标注为已经种树
            treeCount += targetList[2]  #种上希望的树
            print(i, "相离", treeCount)
print(treeCount)
