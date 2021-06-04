# Created by Moontasir Abtahee at 6/2/2021
count = int(input())
result = 0
array = map(int, input().split())
for i in array:
    result = result + i
    result = result * 113

print(result % 10000007)
