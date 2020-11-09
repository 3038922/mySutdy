n = int(input())  # 果子种类
nums = list(map(int, input().split()))  #每种果子的数量
nums.sort()
ps = 0  #体力
numsSet = []
for i in range(0, n, 2):
    if (i + 1 == n):
        numsSet.append([nums[i]])
    else:
        numsSet.append([nums[i], nums[i + 1]])

for it in numsSet:
    if (len(it) == 1):
        ps += it[0]
    else:
        ps += it[0] + it[1]
print(ps)
