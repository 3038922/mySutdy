class Person:
    val = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        self.val += 1
        print(self.name, " ", self.age)
        self.test()
        self.add()

    @classmethod  # 类方法 cls指代类本身
    def add(cls):
        cls.val += 1
        cls.test()

    @staticmethod  # 静态成员函数 跟C++一样
    def test():
        Person.val += 1
        print("this is staticmethod", Person.val)
