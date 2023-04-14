n = int(input())
score = list(map(int, input().split()))
m = max(score)
sum = 0

for i in range(n):
    score[i] = (score[i]/m)*100 
    sum += score[i]

avg = sum/n
print(avg)