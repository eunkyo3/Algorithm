row = 9
col = 9
result_max = 0
result_x = 0
result_y = 0

arr = [list(map(int, input().split())) for _ in range(row)]

for i in range(row):
    for j in range(col):
        if result_max <= arr[i][j]:
            result_max = arr[i][j]
            result_x = i + 1
            result_y = j + 1

print(result_max)
print(result_x, result_y)