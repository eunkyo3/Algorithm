# 학점과 학점에 따른 점수를 나타내는 딕셔너리
grade_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0
}

# 초기화된 총 학점과 결과 변수
total = 0
result = 0

# 20번의 반복을 통해 사용자로부터 입력을 받음
for _ in range(20):
    # 사용자로부터 입력된 문자열을 공백을 기준으로 나누어 리스트로 변환
    s = list(map(str, input().split()))

    # 만약 해당 학점이 'P'가 아니라면 결과에 학점에 해당하는 점수를 곱하고 총 학점에 더함
    if s[2] != 'P':
        result += float(s[1]) * grade_dict[s[2]]
        total += float(s[1])
    else:
        # 학점이 'P'라면 아무 작업을 수행하지 않고 계속 진행
        continue

# 최종 결과를 출력하고 평균을 계산하여 소수점 아래 6자리까지 출력
print('{:.6f}'.format(result/total))
