# Created by Moontasir Abtahee at 6/2/2021
total = int(input())

while True:
    symb , numb = input().split(" ")
    numb = int(numb)
    if symb == "+":
        total += numb
    elif symb == "*":
        total*=numb
    elif symb == "%":
        print(total%numb)
        break

