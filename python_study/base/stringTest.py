import re
test1 = "陈然兮、陈昱安、战前应"
test2 = "汪汪汪"
array = []
array.append(test1)
array.append(test2)
array.append("喵喵 猪猪")
p = re.compile(r'[、， ]')
name = []
for it in array:
    temp = re.split(p, it)
    for it1 in temp:
        it1 = it1.replace("喵喵", "猫猫").replace("战前应", "占倩影")
        name.append(it1)
for it in name:
    print(it)
