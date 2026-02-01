n = int(input())
num_arr = set(map(int, input().split()))
m = int(input())
find_arr = list(map(int, input().split()))

for i in find_arr:
    if i in num_arr:
        print(1)
    else:
        print(0)