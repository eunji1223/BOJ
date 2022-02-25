N=int(input())
dp=[1,2]
for i in range(3,N+1):
    dp.append((dp[i-2]+dp[i-3])%15746)
print(dp[N-1])
    


