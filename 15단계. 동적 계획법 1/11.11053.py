#입력 데이터가 1000개 --> 시간제한 1초, 관습적으로 1000000000개 정도의 연산하면 1초
#이론적으로 O(n^3)알고리즘까지 인정

N=int(input())
A=list(map(int,input().split()))
D=[0]*(N+1)
maxN=0
for i in range(1,N):
    for j in range(0,i):
        if(A[j]<=A[i]):
            if D[j]+1>D[i]:
                D[i]=D[j]+1
            else: D[i]=D[i]
            if maxN<D[i]: maxN=D[i]
print(maxN)
