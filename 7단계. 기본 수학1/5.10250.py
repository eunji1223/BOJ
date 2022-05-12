#H=호텔 층수,W=각 층 방수,N=손님
test=int(input())
for i in range(test):
    result=0
    H,W,N=map(int,input().split())
    result=(N//H)+1
    if N%H==0:
        result=N//H
        result+=H*100
    else:result+=(N%H)*100
    print(result)
    
