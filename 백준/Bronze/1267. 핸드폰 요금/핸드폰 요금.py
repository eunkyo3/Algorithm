n = int(input())

요금 = list(map(int, input().split()))

영식 = 0
민식 = 0

for i in range(n):
    영식 += (요금[i]//30+1)*10
    민식 += (요금[i]//60+1)*15

if 영식 == 민식:
    print(f'Y M {영식}')
elif 영식 > 민식:
    print(f'M {민식}')
else:
    print(f'Y {영식}')