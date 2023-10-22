a, b = map(int, input().split())

합구하는방 = []
result = 0

for i in range(1, b+1):
    for j in range(i):
        합구하는방.append(i)

for i in range(a, b+1):
    result += 합구하는방[i-1]

print(result)