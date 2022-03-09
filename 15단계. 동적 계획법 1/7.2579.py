N=int(input())
S=[0 for _ in range(301)] #값 저장 리스트
D=[0 for _ in range(301)] #계단 최고 값 저장하는 DP리스트
for i in range(N):
    S[i]=int(input())
D[0]=S[0] #첫 계단 값
D[1]=S[0]+S[1] #첫 계단 + 다음 계단 값(1칸 전 계단(최고값)+ 현재 값)
D[2]=max(S[1]+S[2],S[0]+S[2]) #1칸 전 계단, 2칸 전 계단 최고 값 + 현재 값
for i in range(3,N):
    D[i]=max(D[i-3]+S[i-1]+S[i],D[i-2]+S[i])
print(D[N-1])
