dotlist=[]
for i in range(3):
    dotlist.append(list(map(int,input().split())))
xlist=[]
ylist=[]
for [x,y] in dotlist:
    xlist.append(x)
    ylist.append(y)
x=y=0
for y in xlist:
    if xlist.count(y)==1:
        x=y
for z in ylist:
    if ylist.count(z)==1:
        y=z
print(x,y)
