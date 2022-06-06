N,M=map(int,input().split())
num=list(map(int,input().split()))
for i in range(1,len(num)):
    num[i]+=num[i-1]
for j in range(M):
    a,b=map(int,input().split())
    if a-b<1: print(num[b])
    else: print(num[b]-num[a])
