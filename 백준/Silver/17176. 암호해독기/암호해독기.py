n = int(input())
lis = list(map(int, input().split(" ")))
s = input()
number= []
# A~Z = 1-26 -> ord("A") - 64 / a~z = 27-52 -> ord("a") - 70

if len(s) > len(lis):
    print("n")
else:
    for i in s:
        if i.islower():
            number.append(ord(i) - 70)
        elif i.isupper():
            number.append(ord(i) - 64)
        else:
            number.append(0)

    lis.sort()
    number.sort()
    flag = 0

    for i in range(len(lis)):
        if lis[i] != number[i]:
            print("n")
            flag = 1
            break
    if flag == 0:
        print("y")