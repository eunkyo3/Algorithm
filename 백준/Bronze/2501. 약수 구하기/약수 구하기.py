a, b = map(int, input().split())

res = []

for i in range(1, a+1):
    if a % i == 0:
        res.append(i)

if len(res) >= b:
    print(res[b-1])
else:
    print('0')