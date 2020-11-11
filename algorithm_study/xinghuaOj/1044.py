starName = list(map(ord, input().strip()))
groupName = list(map(ord, input().strip()))
totalStat = 1
totalGroup = 1
for it in starName:
    totalStat *= (it - 64)
for it in groupName:
    totalGroup *= (it - 64)
starAws = totalStat % 47
groupAws = totalGroup % 47

if (starAws == groupAws):
    print("GO")
    str = "r1=r2=" + str(groupAws)
    print(str)
else:
    print("STAY")
    str = "r1=" + str(starAws) + " r2=" + str(groupAws)
    print(str)
