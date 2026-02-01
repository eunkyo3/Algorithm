n = int(input())
num_arr = list(map(int, input().split()))
m = int(input())
find_arr = list(map(int, input().split()))
count_dict = {}
result_arr = []

for i in num_arr:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

for i in find_arr:
    result_arr.append(count_dict.get(i, 0))

print(*result_arr)
