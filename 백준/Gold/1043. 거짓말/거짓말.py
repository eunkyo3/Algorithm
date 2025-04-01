def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    parent[b] = a
    return True

n, m = map(int, input().split())
tmp = list(map(int, input().split()))
truth = tmp[1:]

parent = [-1 for _ in range(n + 1)]
party = []

for _ in range(m):
    p = list(map(int, input().split()))[1:]
    party.append(p)
    for i in range(len(p) - 1):
        union(p[i], p[i + 1])

truth_root = set(find(t) for t in truth)

count = 0
for p in party:
    if all(find(person) not in truth_root for person in p):
        count += 1

print(count)