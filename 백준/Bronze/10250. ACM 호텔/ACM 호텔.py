t = int(input())
x = 0
floor = 0

for i in range(t):
    h, w, n = map(int, input().split())
    
    if n % h == 0:
        x = n//h
        floor = h
    else:
        x = n//h + 1
        floor = n % h

    print(floor*100+x)