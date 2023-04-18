sort_list = list(map(int, str(input())))
sort_list.sort(reverse=True)
for i in sort_list:
    print(i, end='')