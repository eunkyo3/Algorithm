n = int(input())

if n == 1:
    print("*")
else:
    for i in range(1, n):
        if i == 1:
            print(" "*(n-i)+"*")
        print(" "*(n-i-1)+"*"+" "*(i*2-1)+"*")