t = int(input())
dic = {}

for _ in range(t):
    name, status = input().split()
    if status == 'enter':
        dic[name] = status
    else:
        del dic[name]

result = sorted(dic.items(), reverse=True)
dic = dict(result)

for key in dic.keys():
    print(key)