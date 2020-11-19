"""
样例输入 Copy
10000
7
4 2 4 3 1 4 6
70 60 50 40 30 20 10

9950

[4, 70]
[2, 60]
[4, 50]
[3, 40]
[1, 30]
[4, 20]
[6, 10]
"""
money = int(input())
games = int(input())
time = list(map(int, input().split()))  #时间
fine = list(map(int, input().split()))  #罚款
timeAndFine = []
for i in range(0, games):
    #timeAndFine.append([time[i], fine[i], fine[i] / time[i], True])
    #以扣款数比例来排序 第二排序以扣钱多到少排序 贪心 但这样答案是错的...
    timeAndFine.append([time[i], fine[i]])
#题解意思是用金额排序....也就是贪心算法本质并不一定是最正确的解法
timeAndFine.sort(key=lambda x: (-x[1], x[0]))  # 扣钱多的先玩 扣钱一样多的花费时间少的先玩

i = 0
for it in timeAndFine:
    print(it)
    if (it[0] > 0):  #如果有时间完成就去完成
        for j in range(i + 1, games):  #完成后，所有能站此座位的的，都少了一座位，就-1。。
            if (it[0] <= timeAndFine[j][0]):  #如果这次时间花的比下次时间少
                timeAndFine[j][0] -= 1
    else:  #没时间，就代表必须扣相应的钱了。
        print(i, "扣钱", it[1])
        money -= it[1]
    i += 1

print(money)
