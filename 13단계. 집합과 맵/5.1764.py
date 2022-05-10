N,M=map(int,input().split())
NL=set()
for i in range(N):
    NL.add(input())
ML=set()
for j in range(M):
    ML.add(input())
same=NL&ML
print(len(same))
same=list(same)
same.sort()
for i in range(len(same)):
    print(same[i])
