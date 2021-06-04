# Created by Moontasir Abtahee at 6/2/2021
count = int(input())
out = []
for i in range(count):
    r = 1
    x , y  = map(int,input().split())
    for i in range(y):
        D = x/r
        r = (r+D)/2

    out.append(r)

for i in out:
    if i%int(i)==0.0:
        print(i,end=" ")
    else:
        print(i,end=" ")
