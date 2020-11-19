import sys
for i in range(1, 8):
    a, b = map(int, input().split())
    if (a + b > 8):
        print(i)
        sys.exit()
print(0)
