# n, b = input().split()
# print(int(n, b))

n, b = input().split()

arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i in enumerate(n[::-1]):
    result += (int(b)**i[0]) * (arr.index(i[1]))
print(result)