모음 = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    cnt = 0

    if s == '#':
        break

    for i in s:
        for j in 모음:
            if i.lower() == j.lower():
                cnt += 1
    
    print(cnt)   