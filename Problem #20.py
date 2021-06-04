# Created by Moontasir Abtahee at 6/2/2021
count = int(input())
for i in range(count):
    string  = input()
    count = 0
    for i in string:
        if i in ["a","e","i","o","u","y"]:
            count+=1

    print(count)