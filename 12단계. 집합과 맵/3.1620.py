import sys
N,M=map(int,sys.stdin.readline().split())
Doc={}
for i in range(1,N+1):
    name=sys.stdin.readline().strip()
    Doc[str(i)]=name
    Doc[name]=i
for j in range(M):
    Q=sys.stdin.readline().strip()
    print(Doc[Q])
