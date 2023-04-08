list1, list2 = [], []
n, m = map(int, input().split())

for i in range(n):
    a = list(map(int, input().split()))
    list1.append(a)

for i in range(n):
    b = list(map(int, input().split()))
    list2.append(b)

for i in range(n):
    for j in range(m):
        print(list1[i][j] + list2[i][j], end=' ')
    print()