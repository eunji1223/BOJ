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

"""
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
print(prefix)
# 나머지가 같은 두 부분합을 고르면 두 구간은 M의 배수가 됨
# 나머지가 0인 경우는 부분합 자체가 M의 배수인 경우이므로 두 구간이 아닌 본인
# 구간도 될 수 있음. INDEX가 0인(부분합 0)인 것을 포
ans=0
for i in prefix:
    print(ans)
    ans+=i*(i-1)//2
print(ans)
""" # 결과 값이 다르게 나옴

"""
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))
# N,M,*A=map(int,open(0).read().split()) 으로도 사용 가능

prefix = [0]*M
s=0
for i in range(N):
    s=(s+A[i])%M
    prefix[s]+=1
ans=0
for i in range(M):
    if i==0: ans+=prefix[i]*(prefix[i]+1)>>1
    else: ans+=prefix[i]*(prefix[i]+1)>>1
print(ans)
""" # 결과 다르게 나옴

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split())) + [0]
prefix=[0]*M

for i in range(N):
    A[i] += A[i-1]
    prefix[A[i]%M]+=1
ans = prefix[0]
for i in prefix:
    ans+=i*(i-1)//2
print(ans)
