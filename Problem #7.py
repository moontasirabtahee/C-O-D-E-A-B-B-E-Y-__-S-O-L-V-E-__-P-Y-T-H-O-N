# Created by Moontasir Abtahee at 6/2/2021
numList = list(map(int,input().split(" ")))
convert = numList[1:]
outList = list()
for i in convert:
    out = (i-32)*5/9
    #print(out)
    outList.append(round(out))

for i in outList:
    print(i,end=" ")

