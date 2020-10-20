arr = []
#n = int(input("请输入数组长度:"))
# 回车式数组输入
# for i in range(n):
#     arr.append(int(input()))

#空格式数组输入
#arr = list(map(int, input().split()))  #split()默认的是去掉空格

#str 字符串类型数据的读取办法
# 回车方式录入
# N = int(input('请输入数组长度:'))
# for i in range(N):
#     s = input().strip().rstrip()  #字符类型的一维数组，建议写 strip()去掉末尾换行符
#     arr.append(s)
# print(arr)

#三、一维数组和二维数组的开设
#arr = [1 for i in range(105)]  #定义的同时初始化
arr = [[1 for i in range(105)] for j in range(105)]  #二维数组定义的同时初始化
print(arr)