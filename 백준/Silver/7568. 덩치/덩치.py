n = int(input())
arr = []
result = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in arr:
    cnt = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    result.append(cnt)

print(*result)