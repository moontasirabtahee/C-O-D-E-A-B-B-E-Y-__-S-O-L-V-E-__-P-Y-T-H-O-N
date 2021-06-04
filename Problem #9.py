# Created by Moontasir Abtahee at 6/2/2021
count = int(input())
output = []
for i in range(count):
    a,b,c = map(int,input().split(" "))
    if a+b>c and a+c>b and b+c>a:
        output.append(1)
    else:
        output.append(0)

for i in output:
    print(i,end=" ")
