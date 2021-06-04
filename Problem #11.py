# Created by Moontasir Abtahee at 6/2/2021
counter = int(input())
OutList = []
for i in range(counter):
    a,b,c = map(int,input().split(" "))
    total = a*b+c
    sum = 0
    while total != 0:
        x = total%10
        sum+=x
        total = total//10

    OutList.append(sum)

for i in OutList:
    print(i,end=" ")


