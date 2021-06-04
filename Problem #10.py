# Created by Moontasir Abtahee at 6/2/2021
counter = int(input())
output = []
for i in range(counter):
    x1,y1,x2,y2 = map(int,input().split(" "))
    a = int( (y1-y2)/(x1-x2))
    b = int(y1-(a*x1))
    output.append((a,b))

for i in output:
    print("("+str(i[0])+" "+str(i[1])+")",end=" ")
