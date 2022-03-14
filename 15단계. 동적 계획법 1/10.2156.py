A=[]
DP=[]
N=int(input())
for i in range(N):
    A.append(int(input()))
if N>1:
    DP.append(A[0])
    DP.append(A[0]+A[1])
if N>2:
    DP.append(max(A[2]+A[1],A[2]+A[0],DP[1]))
for i in range(3,N):
    DP.append(max(DP[i-1],DP[i-3]+A[i-1]+A[i],DP[i-2]+A[i]))
print(DP[N-1])
