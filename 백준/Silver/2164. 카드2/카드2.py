from collections import deque

arr = deque()
n = int(input())

for i in range(n, 0, -1):
    arr.append(i)

while len(arr) > 1:
    arr.pop()
    arr.rotate(1)

print(*arr)