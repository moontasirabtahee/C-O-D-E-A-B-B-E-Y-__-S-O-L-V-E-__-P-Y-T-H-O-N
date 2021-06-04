# Created by Moontasir Abtahee at 6/2/2021
counter = int(input())
outArray = list()
for i in range(counter):
    array = list(map(int,input().split()))
    Average = sum(array)/(len(array)-1)
    outArray.append(round(Average))

for i in outArray:
    print(i ,end= " ")