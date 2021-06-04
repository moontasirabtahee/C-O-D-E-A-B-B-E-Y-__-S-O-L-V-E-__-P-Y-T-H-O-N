# Created by Moontasir Abtahee at 6/2/2021
count = int(input())
out = []
for i in range(count):
    out = 1
    string = input()
    checker = list()
    for i in string:
        if (i == '(' or i == '[' or i == '{' or i == '<'):
            checker.append(i)
            # print(checker)
        if i == ")":
            if not checker:
                out = 0
                break
            elif checker[-1] == '(':
                checker.pop()
            else:
                out = 0
                break

        elif i == '}':
            if not checker:
                out = 0
                break

                
            elif checker[-1] == "{":
                checker.pop()
            else:
                out = 0
                break
        elif i == "]":
            if not checker:
                out = 0
                break
            elif checker[-1] == '[':
                checker.pop()
            else:
                out = 0
                break

        elif i == ">":
            if not checker:
                out = 0
                break
            elif checker[-1] == "<":
                checker.pop()
            else:
                out = 0
                break


    if checker:
        out = 0

    print(out)





