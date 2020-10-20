n, k = map(int, input().split())
arr = list(set(map(int, input().split())))
if (k <= len(arr)):
    print(arr[k - 1])
else:
    print("No result")
