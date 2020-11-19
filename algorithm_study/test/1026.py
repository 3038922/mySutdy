n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = 0  #相当于一个中间量
num = -1  #去重后的实际下标
while (temp < n):  #跳着遍历比较快
    num += 1  #实际arr后移
    arr[num] = arr[temp]  #把第I个数赋值给num
    nextNum = temp + 1  # nextNum表示i元素的下一个
    while (nextNum < n and arr[nextNum] == arr[temp]):  #nextNum<n 防止超限 且 当前这个和后一个一样
        nextNum += 1  #遍历查找元素后移到哪里
    temp = nextNum  #把后移后的位置坐标给temp

if (num + 1 < k):  #如果
    print("No result")
else:
    print(arr[k - 1])
"""
只能ac 90%
n, k = map(int, input().split())
arr = list(set(map(int, input().split())))
if (len(arr) < k or len(arr) < n):
    print("No result")
else:
    print(arr[k - 1])
"""