n = int(input())
list1 = list(input())
for i in range(n-1):
    x = list(input())
    for j in range(len(list1)):
        if list1[j] != x[j]:
            list1[j] = '?'
for i in range(len(list1)):
    print(list1[i], end='')

# print(''.join(list1)) <-- join함수로 가능