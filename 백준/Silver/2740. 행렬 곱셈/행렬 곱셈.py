# 첫 번째 행렬의 크기 입력
m1, n1 = map(int, input().split())

# 첫 번째 행렬 입력
matrix1 = [list(map(int, input().split())) for i in range(m1)]

# 두 번째 행렬의 크기 입력
m2, n2 = map(int, input().split())

# 두 번째 행렬 입력
matrix2 = [list(map(int, input().split())) for i in range(m2)]

# 결과 행렬 초기화
result_matrix = [[0] * n2 for _ in range(m1)]

# 행렬 곱셈 수행
for i in range(m1):
    for j in range(n2):
        result = 0
        for x in range(m2):
            result += matrix1[i][x] * matrix2[x][j]
        result_matrix[i][j] = result

# 결과 행렬 출력
for row in result_matrix:
    print(*row)