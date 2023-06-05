import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x = float(input())
    arr.append(x)

sorted_arr = sorted(arr)[:7]
for value in sorted_arr:
    print(f"{value:.3f}")