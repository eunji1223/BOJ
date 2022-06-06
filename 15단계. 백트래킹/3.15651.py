N,M=map(int,input().split())
num=[]
def printN(depth):
    if depth==M:
        print(' '.join(map(str,num)))
        return
    for i in range(N):
        num.append(i+1)
        printN(depth+1)
        num.pop()
printN(0)
