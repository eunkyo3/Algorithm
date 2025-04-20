def find(x):
    if arr[x] < 0:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    arr[b] = a
    return True

n, m = map(int, input().split())
arr = [-1] * (n + 1)

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    elif c == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
