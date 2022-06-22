"""
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))
sumA=[0]
for i in range(len(A)):
    sumA.append(sumA[i]+A[i])

count=0
for i in range(len(sumA)):
    for j in range(i+1,len(sumA)):
        if (sumA[j]-sumA[i])%3==0:
            count+=1
print(count)
""" # 당연히 시간초과남

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))

prefix = [0 for i in range(M)]
s=0

prefix[0]=1
for i in range(N):
    s+=A[i]
    prefix[s%M]+=1
ans=0
for i in prefix:
    ans+=i*(i-1)//2
print(ans)
