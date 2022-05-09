count=0
N,M=map(int,input().split())
NL=set()
ML=list()
for i in range(N):
    NL.add(input())
for i in range(M):
    str=input()
    if (str in NL)==True:
        count+=1
print(count)
