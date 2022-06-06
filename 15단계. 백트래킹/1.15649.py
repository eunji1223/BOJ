"""
out=[]
visited=[False]*N
def visit(depth,N,M):
    if depth==M:
        print(' '.join(map(str,out)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            out.append(i+1)
            visit(depth+1,N,M)
            visited[i]=False
            out.pop()
visit(0,N,M)
"""

N,M=map(int,input().split())
number=[]
visited=[False]*N
def printN(depth):
    global N,M
    if depth==M:
        print(' '.join(map(str,number)))
        return
    for i in range(N):
        if visited[i]==False:
            visited[i]=True
            number.append(i+1)
            printN(depth+1)
            visited[i]=False
            number.pop()
printN(0)
