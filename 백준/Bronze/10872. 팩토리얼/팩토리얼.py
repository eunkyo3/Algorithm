n = int(input())
factorial = 1
if n == 0:
    print('1')
else:
    for i in range(n):
        factorial *= i + 1
    print(factorial)