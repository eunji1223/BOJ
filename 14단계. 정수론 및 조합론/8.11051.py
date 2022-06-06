N,K=map(int,input().split())
sumN=1
sumK=1
for i in range(1,K+1):
    sumN*=N
    sumK*=i
    N-=1
print((sumN//sumK)%10007)
