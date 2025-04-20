from collections import deque

n, k = map(int, input().split())

arr = deque(range(1, n + 1))
result = []

while arr:
    arr.rotate(-(k - 1))
    result.append(arr.popleft())

print(f"<{', '.join(map(str, result))}>")
