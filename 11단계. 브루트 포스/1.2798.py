N,M=map(int,input().split())
A=list(map(int,input().split()))
result=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if A[i]+A[j]+A[k]>M:
                continue
            else:
                result=max(result,A[i]+A[j]+A[k])
print(result)
"""
def find(k,c):
    global N,M,maxS,number,x
    currentS=0
    for i in range(N):
        if x[i]==1:
            currentS+=number[i]
    if k==N:return
    if c==3:
        if currentS>maxS:
            maxS=currentS
            print(x)
    else:
        if currentS+number[k]<=M and c<=3:
            x[k]=1
            c+=1
            if currentS+number[k]==M and c==3: 
                maxS=M
                return 
            else:
                find(k+1,c)
            x[k]=0
            c-=1
            find(k+1,c)
maxS=0
N,M=map(int,input().split())
number=list(map(int,input().split()))
x=[]
for i in range(N):
    x.append(0)
find(0,0)
print(maxS)
"""

