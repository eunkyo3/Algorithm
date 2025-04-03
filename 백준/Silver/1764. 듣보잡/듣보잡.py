n, m = map(int, input().split())

no_listen = set()
no_see = set()

for _ in range(n):
    no_listen.add(input())

for _ in range(m):
    no_see.add(input())

no_all = no_listen & no_see

print(len(no_all))
print(*sorted(no_all), sep='\n')