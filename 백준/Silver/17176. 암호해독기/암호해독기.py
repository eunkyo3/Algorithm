n = int(input())

numlist = list(map(int, input().split()))
s = input()
encryption = []

if len(numlist) != len(s):
    print('n')
else:
    for i in s:
        if i.isupper():
            encryption.append(ord(i) - 64)
        elif i.islower():
            encryption.append(ord(i) - 70)
        elif i == ' ':
            encryption.append(0)

    numlist.sort()
    encryption.sort()
    flag = 0

    for i in range(n):
        if numlist[i] != encryption[i]:
            print('n')
            flag = 1
            break
    if flag == 0:
        print('y')