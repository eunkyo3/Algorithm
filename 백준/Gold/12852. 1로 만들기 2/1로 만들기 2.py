n = int(input())
x = [0] * (n+1)
path = []
cur = n

for i in range(2, n+1):
    x[i] = x[i-1]+1
    
    if i%2 == 0:
        x[i] = min(x[i], x[i//2]+1)
    
    if i%3 == 0:
        x[i] = min(x[i], x[i//3]+1)

while True:
    path.append(cur)

    if cur == 1:
        break

    if cur % 3 == 0 and x[cur] - x[cur//3] == 1:
        cur //= 3
    elif cur % 2 == 0 and x[cur] - x[cur//2] == 1:
        cur //=2
    elif x[cur] - x[cur-1] == 1:
        cur -=1

print(x[n])
print(*path)