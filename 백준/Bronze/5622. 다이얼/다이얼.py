# 다이얼 알파벳 그룹을 정의한 리스트
다이얼 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# 사용자로부터 알파벳 문자열을 입력받음
알파벳 = input()

# 결과를 저장할 변수 초기화
result = 0

# 입력된 알파벳 문자열을 한 글자씩 처리
for i in range(len(알파벳)):
    # 다이얼 그룹을 순회
    for j in 다이얼:
        # 현재 알파벳이 현재 다이얼 그룹에 속한지 확인
        if 알파벳[i] in j:
            # 해당 다이얼 그룹의 인덱스를 찾고, 3을 더해서 결과에 누적
            result += 다이얼.index(j) + 3

# 결과 출력
print(result)
