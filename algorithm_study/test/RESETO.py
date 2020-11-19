def getKstr(arr, n, k):
    for i in range(2, len(arr)):
        if arr[i]:  #看看对应表是否FALSE掉
            p = i
            while p < len(arr):  #当P小于N+1的时候
                if arr[p]:
                    arr[p] = False
                    k -= 1
                    if k == 0:
                        return p
                p += i  #i的倍数都被筛掉 不用一个个的%了


n, k = map(int, input().split())
arr = [True for x in range(n + 1)]  #初始化了一堆TRUE的表 省的earse了
print(getKstr(arr, k))