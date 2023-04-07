n = int(input())
for i in range(n):
    num, str = input().split()
    num = int(num)
    for j in str:
        print(j*num,end='')
    print()