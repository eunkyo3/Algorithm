arr = []

n = int(input())  

for _ in range(n):
    arr.append(list(map(int, input().split())))  # map 객체를 리스트로 변환

arr = sorted(arr)

for item in arr:
    print(*item)