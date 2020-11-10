n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
count = 1
row = 0  #行
col = n - 1  #列
loop = 0  #循环次数
flag = n * n
while (count <= n * n):
    if (n * n % 2 == 0):
        flag = n * n + 1
    arr[row][col] = count  #设置启始坐标
    row += 1
    count += 1
    while (row < n - 1 - loop and count < flag):
        """
        下
        """
        arr[row][col] = count
        row += 1
        count += 1
    while (col > loop and count < flag):
        """
        左
        """
        arr[row][col] = count
        col -= 1
        count += 1
    while (row > loop and count < flag):
        """
        上
        """
        arr[row][col] = count
        row -= 1
        count += 1
    while (col < n - 1 - loop and count < flag):
        """
        右
        """
        arr[row][col] = count
        col += 1
        count += 1
    row += 1
    col -= 1
    loop += 1
for i in range(0, n):
    for j in range(0, n):
        print(arr[i][j], end=' ')
    print("")