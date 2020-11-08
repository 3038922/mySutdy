def test1():
    """
    普通输入 输入2位小数
    """
    a = []
    N = int(input())
    for i in range(N):
        a.append(float(input()))
    for it in a:
        print("%.2f" % it, end=' ')


def test2():
    """
    整行输入测试
    """
    a = list(map(float, input().split()))  # split()默认是去掉空格
    for it in a:
        print("%.2f" % it, end=' ')


def test3():
    """
    字符串输入测试
    """
    A = []
    N = int(input())
    for i in range(N):
        """
        strip() 于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        """
        s = input().strip()
        s.rstrip()  #删除 string 字符串末尾的指定字符（默认为空格）.
        A.append(s)
    for it in A:
        print(it, end=" ")


def test4():
    """
    二维数组和排序
    这样就建好了结构体，排序 sort()使用起来需要记一下格式
    A.sort(key=lambda x:(x[0],x[1]))
    这样写的话，就意味着 A[]数组的第一维由小到大，当第一维度相同的时候，第二维度也是由小到大，那
    么想要由某一维度由大到小的话，只需要在前面加个减号”-”符号即可，如下：
    A.sort(key=lambda x:(x[0],-x[1]))
    这样写的话，就意味着 A[]数组的第一维由小到大，当第一维度相同的时候，第二维度是由大到小。Python
    的时效不是很好，所以对于排序来说的，如果能数据范围不大的话还是建议计数排序。
    """
    matrix = [[112, 2, 3], [4, 5444, 6], [22, 33, 44]]
    # x = []
    # y = []
    # A = []
    # N = 4  #4行
    # for i in range(N):
    #     x, y = map(int, input().split())
    #     x.append(x)  #此处需要追加的形式，否则库函数不起作用
    #     y.append(i)
    #     A = list(zip(x, y))  #此时就在捆绑,并强制转换成列表 list
    for it in matrix:
        it.sort(reverse=True)
    for it in matrix:
        print(it, " ")


def test5():
    n = int(input())
    count = 1
    for i in range(1, n + 1):  # 注意空格 1开始不要0开始
        for j in range(i):
            print(count, end='')
            count += 1
            if (count > 9):
                count = 0
        print()


def test6():
    maxTime = 8
    sadlyDay = 1
    for i in range(1, 8):
        x, y = map(int, input().split())
        if (x + y > maxTime):
            maxTime = x + y
            sadlyDay = i
    print(sadlyDay)


def test7():
    x, y = map(int, input().split())
    count = 0
    for i in range(x, y + 1):
        count += str(i).count('2')
    print(count)


def test8():
    n, k = map(int, input().split())
    arr = list(set(map(int, input().split())))
    if (len(arr) < k):
        print("No result")
    else:
        print(arr[k - 1])
