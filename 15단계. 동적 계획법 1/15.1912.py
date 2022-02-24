
"""최대구간합(간단한 방법) --> 따라서 시간초과(O(n^2))
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
"""
