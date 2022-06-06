"""
import math
n,m=map(int,input().split())
r=math.factorial(n)//(math.factorial(m)*math.factorial(n-m))
strr=str(r)
count=0
for i in range(len(strr)-1,-1,-1):
    if strr[i]!='0':
        break
    count+=1
print(count)
#--> 단순 팩토리얼 이용으로 시간초과
"""

#0 --> 2*5, 10의 경우 2*5, 100의 경우 2*2*5*5
def counts(n):
    sec=0
    while n!=0:
        n=n//2
        sec+=n
    return sec

def countf(n):
    fif=0
    while n!=0:
        n=n//5
        fif+=n
    return fif

n,m=map(int,input().split())
print(min(counts(n)-counts(m)-counts(n-m), countf(n)-countf(m)-countf(n-m)))

