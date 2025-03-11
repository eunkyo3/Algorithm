def gcd(a, b):
    if b == 0:
        return a
    
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    c = gcd(a, b)
    print((a*b)//c)