t = int(input())

dp = [0] * 11
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

save = 4

for _ in range(t):
    n = int(input())
    if save <= n:
        for i in range(save, n + 1): 
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        save = n + 1  
    print(dp[n])