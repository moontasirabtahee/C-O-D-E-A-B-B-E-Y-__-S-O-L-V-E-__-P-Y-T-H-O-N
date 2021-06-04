# Created by Moontasir Abtahee at 6/2/2021
length = int(input())
outList = list()
for i in range(length):
    numList = list(map(int,input().split(" ")))
    output = numList[0]/numList[1]
    if output-(numList[0]//numList[1]) == 0.5:
        output+=0.5
    outList.append(round(output))
for i in outList:
    print(i,end=" ")