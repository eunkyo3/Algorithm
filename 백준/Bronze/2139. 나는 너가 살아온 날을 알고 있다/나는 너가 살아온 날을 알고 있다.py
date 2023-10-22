while True:
    day, month, year = map(int, input().split())
    
    if year == 0 and month == 0 and day == 0:
        break

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days_in_month[2] = 29

    total_days = sum(days_in_month[:month]) + day

    print(total_days)