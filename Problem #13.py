# Created by Moontasir Abtahee at 6/2/2021
counter = int(input())
outList = list()
array = map(int,input().split())
for i in array:
    sum  = 0
    flag = 1
    for x in str(i):
        sum+= int(x)*flag
        flag+=1

    outList.append(sum)

for i in outList:
    print(i,end=" ")