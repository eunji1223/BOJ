N=int(input())
AN=list(map(int,input().split()))
p,m,mu,d=map(int,input().split())
maxN,minN=-100000000,100000000

def sol(A,i,p,m,mu,d):
    global maxN,minN
    if i==N:
        maxN=max(maxN,A)
        minN=min(minN,A)
        return
    if p>0:
        sol(A+AN[i],i+1,p-1,m,mu,d)
    if m>0:
        sol(A-AN[i],i+1,p,m-1,mu,d)
    if mu>0:
        sol(A*AN[i],i+1,p,m,mu-1,d)
    if d>0:
        sol(int(A/AN[i]),i+1,p,m,mu,d-1)

sol(AN[0],1,p,m,mu,d)
print(maxN)
print(minN)
