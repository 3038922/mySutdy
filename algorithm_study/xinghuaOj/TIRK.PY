line = list(input())
n = 1
for it in line:
    if (it == "A"):
        if (n == 1):
            n = 2
        elif (n == 2):
            n = 1
        else:
            print("A error")
    elif (it == "B"):
        if (n == 2):
            n = 3
        elif (n == 3):
            n = 2
        else:
            print("B error")
    elif (it == "C"):
        if (n == 3):
            n = 1
        elif (n == 1):
            n = 3
        else:
            print("C error")
print(n)
