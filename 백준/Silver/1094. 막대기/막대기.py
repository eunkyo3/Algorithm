n = 64
x = int(input())
cnt = 0
while True:
    if n <= x:
        x -= n
        cnt += 1
    n //= 2

    if n == 0:
        break
print(cnt)