a,b = map(int,input().split())
c = 45-b
if c<0:print("%d %d"%(a,b-45))
elif c==0: print("%d %d"%(a,b-45))
else:
    if a==0:a=24
    print("%d %d"%(a-1,60-c))
