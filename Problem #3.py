# Created by Moontasir Abtahee at 6/2/2021
length = int(input())
outList = list()
for i in range(length):
    numList = list(map(int,input().split(" ")))
    outList.append(sum(numList))

for i in outList:
    print(i,end=" ")