N,M=map(int,input().split())
Doc={}
for i in range(1,N+1):
    name=input()
    Doc[str(i)]=name
    Doc[name]=i
for j in range(M):
    Q=input()
    print(Doc[Q])
