n, c = map(int, input().split())

arr = list(map(int, input().split()))
set_arr = []
count_arr = []
result = []

for i in arr:
    if i in set_arr:
        pass
    else:
        set_arr.append(i)

for i in range(len(set_arr)):
    count_arr.append(arr.count(set_arr[i])) 

for i in range(len(count_arr)):
    max_num = max(count_arr)
    max_num_index = count_arr.index(max_num)

    for i in range(max_num):
        result.append(set_arr[max_num_index])
    
    count_arr[max_num_index] = 0

print(*result)