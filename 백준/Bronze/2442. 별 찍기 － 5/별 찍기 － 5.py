x = int(input())

for i in range(1, x+1):
    for j in range(x, i, -1):
        print(' ', end='')
    for j in range(0, 2 * i - 1):
        print('*', end='')
    print()