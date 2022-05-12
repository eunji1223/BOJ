#아직 해결 X
def binary(n,N,start,end):
    if start>end:
        return 0
    m=(start+end)//2
    if n==N[m]:
        return N[start:end+1].counnt(n)
    elif n<N[m]:
        return binary(n,N,start,m-1)
    else:
        return binary(n,N,m+1,end)

N=int(input())
M=int(input())
D={}
for i in N:
    start=0
    end=len(N)-1
    if i not in D:
        D[i]=binary(n,N,start,end)
