n, b = map(int, input().split())

arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''

while n:
    res += arr[n%b]
    n //= b

res = res[::-1]

print(res)