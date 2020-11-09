import heapq  #堆模块

n = int(input())  # 果子种类
temp = list(map(int, input().split()))  #每种果子的数量
nums = []
ps = 0  #体力
for it in temp:
    heapq.heappush(nums, it)

while (True):
    if (len(nums) > 2):
        temp = heapq.heappop(nums) + heapq.heappop(nums)
        ps += temp
        heapq.heappush(nums, temp)
    else:
        ps += heapq.heappop(nums) + heapq.heappop(nums)
        break

print(ps)
# print(ps)3