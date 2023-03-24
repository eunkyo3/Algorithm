H, M = map(int, input().split()) # h는 시간 m은 분

if H == 0:
    if M < 45:
        H = 23
        M = (60+M)-45
    else:
        M -= 45
else:
    if M < 45:
        H -= 1
        M = (60+M)-45
    else:
        M -= 45

print(H, M)   # 시와 분 출력