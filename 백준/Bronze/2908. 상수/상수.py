s1, s2 = map(str, input().split())

s1 = s1[::-1]
s2 = s2[::-1]

rst = 0

if int(s1)>int(s2):
    rst = s1
else:
    rst = s2

print(rst)