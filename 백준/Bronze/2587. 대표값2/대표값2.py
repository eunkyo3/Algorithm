import statistics

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

print((n1+n2+n3+n4+n5)//5)

middle_num = []

middle_num.append(n1)
middle_num.append(n2)
middle_num.append(n3)
middle_num.append(n4)
middle_num.append(n5)

print(int(statistics.median(middle_num)))