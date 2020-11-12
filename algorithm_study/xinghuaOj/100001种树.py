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
    targetList[i].append(0)
targetList.sort(key=lambda x: (-x[1], -x[2]))

treeCount = 0

for i in range(hopeNums - 1):
    needTree = targetList[i][2] - targetList[i][3]  # 需要定义每段区间还需要种多少树
    # for 循环那些树的区间 有多少树
    if (needTree > 0):  #如果还需要种树
        if (targetList[i][0] <= targetList[i + 1][1]):  #如果本次的端点和下次端点相交
            targetList[i][3] += 1  #给当前的路种树
            targetList[i + 1][3] += 1  #给相交的路种树
            treeCount += targetList[i][3]  #统计树的数量
            print("i:", i, "相交或者相切", treeCount)
        else:
            targetList[i][3] += targetList[i][2]  #直接种2棵树
            treeCount += targetList[i][3]  #统计树的数量
            print("i:", i, "相离", treeCount)
        i += 1

print(treeCount)
