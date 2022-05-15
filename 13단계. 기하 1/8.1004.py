"""
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
"""

t = int(input())
for i in range(t):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for i in range(n):
        px, py, pr = map(int, input().split())
        d1 = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5 #행성 중심 - 시작점 거리
        d2 = (((x2 - px) ** 2) + ((y2 - py) ** 2)) ** 0.5 #행성 중심 - 도착점 거리
        if (d1 < pr and d2 > pr) or (d1 > pr and d2 < pr):#시작점이나 도착점이 원 안에 있다
            cnt += 1
    print(cnt)
