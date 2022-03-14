N=int(input())
A=[]
DP=[0]*N
for i in range(N):
    A.append(int(input()))
DP[0]=A[0]
if N>1:
    DP[1]=A[0]+A[1]
if N>2:
    DP[2]=max(A[2]+A[1],A[2]+A[0],DP[1])
for i in range(3,N):
    DP[i]=max(DP[i-1],DP[i-3]+A[i-1]+A[i],DP[i-2]+A[i])
print(DP[N-1])
