arr = []
for i in range(int(input())):
    arr.append(input())

arr.sort() # 알파벳 순으로 정렬
arr.sort(key=len) # key-point 길이 순 정렬

result = list(dict.fromkeys(arr)) # 순서 유지, 중복 제거

for i in result:
    print(i)