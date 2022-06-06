
"""
#최대구간합(간단한 방법) --> 따라서 시간초과(O(n^2))
def max_sum(A):
    P=[0]
    sum=0
    for a in A:
        sum+=a
        P.append(sum)
    max=-99999999
    for i in range(1,len(P)):
        for j in range(i,len(P)):
            if max<(P[j]-P[i-1]):
                max=P[j]-P[i-1]
    return max
num=int(input())
numlist=list(map(int,input().split()))
sol=max_sum(numlist)
print(sol)
------------------------------------------------------
#divide&conquer 방식 --> 시간초과
def max_sum(A,left,right):
    if left>=right: return A[left]
    m=(left+right)//2
    L=max_sum(A,left,m)
    R=max_sum(A,m+1,right)
    M=A[m]+A[m+1]
    Ml=Mr=-99999
    s=0
    for i in range(m,-1,-1):
        s+=A[i]
        if s>Ml:
            Ml=s
    s=0
    for j in range(m+1,right+1):
        s+=A[j]
        if s>Mr:
            Mr=s
    M=Mr+Ml
    return max(L,M,R)

num=int(input())
numlist=list(map(int,input().split()))
sol=max_sum(numlist,0,num-1)
print(sol)
"""
n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))

