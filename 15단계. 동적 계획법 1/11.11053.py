L=0
for i in range(1,n-1):
    low=1
    high=L
    while low<=high:
        mid=(low+high)//2
        if A[M[mid]]<A[i]:low=mid+1
        else:high=mid-1
    newL=low
    M[newL]=i
    parent[k]=M[newL-1]
    L=max(L,newL)
    
