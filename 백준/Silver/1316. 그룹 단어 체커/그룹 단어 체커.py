n = int(input()) # 단어의 수
cnt = 0 # 그룹 단어 체커의 수
for i in range(n):
    str = input() # 단어를 입력받음
    result = True # 그룹 단어인지 확인
    for j in range(len(str)-1): 
        if str[j] != str[j+1]: # 현재 글자와 다음 글자가 다를때
            if str[j] in str[j+1:]: # 현재 글자가 다음 나머지 글자중에 똑같은게 있을때
                result = False # 그룹 단어가 아님
                break # 아니니까 멈춤
    if result: # 그룹 단어니까 +1
        cnt += 1
print(cnt) # 그룹 단어 개수 출력