t = int(input())

member = []

for _ in range(t):
    age, name = map(str, input().split())
    member.append((int(age), name))

member.sort(key=lambda x: x[0], reverse=False)

for i in member:
    print(i[0], i[1])