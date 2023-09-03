s = input()

op = ['+', '-' , '*', '/']

for i in range(len(s)):
    if s[i] in op and i != 0:
        o = s[i]
        a = int(s[0:i], 8)
        b=  int(int(s[i+1:], 8))
        break

try:
    if o == '+':
        result = oct(a+b)
    elif o == '-':
        result = oct(a-b)
    elif o == '*':
        result = oct(a*b)   
    elif o == '/':
        result = oct(a//b)

    print(int(result.replace('o', '')))

except:
    print('invalid')