h, m = map(int, input().split()) # h는 시간 m은 분
t = int(input()) # 걸리는 시간

h = int(((h*60)+m+t)/60) # 시 표현
m = int(((h*60)+m+t)%60) # 분 표현

if(h > 23): # 시가 24가 되면 0부터 다시 표현
    h = h - 24 

print(h, m) # 시간 출력