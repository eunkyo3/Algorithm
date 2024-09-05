from collections import deque

T = int(input()) 
numbers = list(map(int, input().split()))

dq = deque(numbers)
idx_dq = deque(range(1, T+1)) 

result = []

for i in range(T):
    num = dq.popleft()        
    result.append(idx_dq.popleft()) 
    if num > 0:
        dq.rotate(-(num-1))   
        idx_dq.rotate(-(num-1))
    else:
        dq.rotate(-num)       
        idx_dq.rotate(-num)   

print(*result)