A=[]
DP=[]
N=int(input())
for i in range(N):
    A.append(int(input()))
if N>1:
    DP.append(A[0]+A[1])
for i in range(2,N+1):
    DP.append(max(DP[i-1],DP[i-3]+A[i-1]+A[i],DP[i-2]+A[i]))
print(DP[N-1])
