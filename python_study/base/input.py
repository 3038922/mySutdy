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


test3()