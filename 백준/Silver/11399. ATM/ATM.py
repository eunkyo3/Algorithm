res = []
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

res.append(arr[0])

for i in range(1, n):
    res.append(res[-1] + arr[i])

print(sum(res))