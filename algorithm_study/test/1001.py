arr = [0, 1, 2, 4]
num = int(input())
for i in range(4, num + 1):
    arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])
print(arr[num])
