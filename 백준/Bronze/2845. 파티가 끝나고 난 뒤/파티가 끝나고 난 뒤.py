l, p = map(int, input().split())

x = list(map(int, input().split()))

for i in range(len(x)):
    x[i] -= l*p

print(*x)