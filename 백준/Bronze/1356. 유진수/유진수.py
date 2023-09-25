# 사용자로부터 입력을 받습니다.
n = input()

# 결과 변수 초기화
rst = 0

# 문자열을 두 부분으로 나누기 위한 루프
for i in range(1, len(n)):
    # 현재 인덱스 i를 기준으로 문자열을 두 부분으로 나눕니다.
    s1 = n[:i]
    s2 = n[i:]

    # 각 부분 문자열의 곱을 계산하기 위한 변수 초기화
    rst1 = 1
    rst2 = 1

    # 첫 번째 부분 문자열의 각 숫자를 곱합니다.
    for i in s1:
        rst1 *= int(i)

    # 두 번째 부분 문자열의 각 숫자를 곱합니다.
    for i in s2:
        rst2 *= int(i)

    # 두 부분 문자열의 곱이 서로 같으면 rst를 1로 설정합니다.
    if rst1 == rst2:
        rst = 1

# rst 값에 따라 'YES' 또는 'NO'를 출력합니다.
print("YES" if rst else "NO")
