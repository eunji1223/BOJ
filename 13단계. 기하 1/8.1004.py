t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    loc=[]
    count=0
    for j in range(n):
        cx,cy,r=map(int,input().split())
        if cx-r<=x1 and x1<=cx+r and cy-r<=y1 and y1<=cy+r:
            if cx-r<=x2 and x2<=cx+r and cy-r<=y2 and y2<=cy+r:
                continue
            else:
                count+=1
        elif cx-r<=x2 and x2<=cx+r and cy-r<=y2 and y2<=cy+r:
            if cx-r<=x1 and x1<=cx+r and cy-r<=y1 and y1<=cy+r:
                continue
            else:
                count+=1
    print(count)
