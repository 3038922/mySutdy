# 排序
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

# 列表推倒
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

# 断言
mylist = ['item']
assert len(mylist) >= 2
mylist.pop()
