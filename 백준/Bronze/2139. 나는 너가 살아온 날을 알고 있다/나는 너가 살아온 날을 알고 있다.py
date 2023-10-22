while True:
    d, m, y = map(int, input().split())
    month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    result = 0

    if y == 0 and m == 0 and d == 0:
        break

    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        if m > 2:  
            result += 1

    for i in range(m):
        result += month_day[i]

    result += d

    print(result)