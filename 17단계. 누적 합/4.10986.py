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
# 나머지가 같은 두 부분합을 고르면 두 구간은 M의 배수가 됨
# 나머지가 0인 경우는 부분합 자체가 M의 배수인 경우이므로 두 구간이 아닌 본인
# 구간도 될 수 있음. INDEX가 0인(부분합 0)인 것을 포
ans=0
for i in prefix:
    ans+=i*(i-1)//2 #이 부분
print(ans)

