import sys
input = sys.stdin.readline
N,K=map(int,input().split())
num=list(map(int,input().split()))
max=0
numS=[0]
for i in range(1,N):
    numS.append(numS[i-1]+num[i])
for i in range(N-K+1):
    if numS[i+K]-numS[i]>max:
        max=numS[i+K]-numS[i]
print(max)
