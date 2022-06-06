N,M=map(int,input().split())

num=[]
def printN(depth):
    if depth==M:
        print(' '.join(map(str,num)))
        return
    for i in range(N):
        if depth>0:
            if num[depth-1]<=i+1:
                num.append(i+1)
                printN(depth+1)
                num.pop()
        else:
            num.append(i+1)
            printN(depth+1)
            num.pop()
printN(0)
