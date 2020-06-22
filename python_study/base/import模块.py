import funTest
import sys
import classTest


print(sys.path)
p1 = classTest.Person("aa", 11)
p1.showInfo()
p2 = classTest.Person("vv", 12)
print(p2.name, " ", p2.age)
funTest.sunTest(112121, 33)
p1.add()
p1.test()
p2.test()
p1.test()
