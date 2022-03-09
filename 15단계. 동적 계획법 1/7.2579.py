N=int(input())
S=[0 for _ in range(301)]
D=[0 for _ in range(301)]
for i in range(N):
    S[i]=int(input())
D[0]=S[0]
D[1]=S[0]+S[1]
D[2]=max(S[1]+S[2],S[0]+S[2])
for i in range(3,N):
    D[i]=max(D[i-3]+S[i-1]+S[i],D[i-2]+S[i])
print(D[N-1])
