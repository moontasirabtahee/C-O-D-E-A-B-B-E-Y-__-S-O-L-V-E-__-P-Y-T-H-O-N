# Created by Moontasir Abtahee at 6/2/2021
def sumofAP(first,step,Number):
    Sum = 0
    for i in range(Number):
        Sum += first+(i*step)

    print(Sum,end=" ")

Counter = int(input())
for i in range(Counter):
    a,b,n = map(int,input().split(" "))
    sumofAP(a,b,n)