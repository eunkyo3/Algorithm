chess = [1, 1, 2, 2, 2, 8]

A = list(map(int, input().split()))
for i in range(6):
    print(chess[i]-A[i],end=" ")