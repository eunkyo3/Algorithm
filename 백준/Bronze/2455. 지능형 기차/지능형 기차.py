result = 0
x = 0

for _ in range(4):
    a, b = map(int, input().split())
    x += b - a
    result = max(result, x)

print(result)