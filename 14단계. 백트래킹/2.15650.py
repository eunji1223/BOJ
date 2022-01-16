N,M=map(int,input().split())

number=[]
visited=[False]*N
def printN(depth):
    if depth==M:
        print(' '.join(map(str,number)))
        return
    for i in range(N):
        if visited[i]==False:
            if depth>0:
                if number[depth-1]<i+1:
                    visited[i]=True
                    number.append(i+1)
                    printN(depth+1)
                    visited[i]=False
                    number.pop()
            else:
                visited[i]=True
                number.append(i+1)
                printN(depth+1)
                visited[i]=False
                number.pop()
printN(0)
