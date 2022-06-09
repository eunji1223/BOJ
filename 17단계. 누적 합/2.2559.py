import sys
input = sys.stdin.readline
N,K=map(int,input().split())
num=list(map(int,input().split()))
max=0
for i in range(N-K+1):
    if num[i]+num[i+1]>max:
        max=num[i]+num[i+1]
print(max)
