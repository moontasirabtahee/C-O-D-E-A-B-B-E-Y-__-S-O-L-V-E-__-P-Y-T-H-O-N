# Created by Moontasir Abtahee at 6/2/2021
counter = int(input())
outList = list()
for i in range(counter):
    day1, hour1, min1, sec1, day2, hour2, min2, sec2 = map(int, input().split())
    Start = day1*24*60**2+hour1*60**2+min1*60+sec1
    End = day2*24*60**2+hour2*60**2+min2*60+sec2
    difference = End -Start
    day = difference // (24 * 3600)
    difference = difference % (24 * 3600)
    hour = difference // 3600
    difference %= 3600
    minutes = difference // 60
    difference %= 60
    seconds = difference
    outList.append((day, hour, minutes, seconds))

for i in outList:
    print("("+str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(i[3])+")",end=" ")