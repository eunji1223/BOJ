test=int(input())
dot=[]
for i in range(test):
    dot.append(list(map(int,input().split())))
dot.sort()
for [x,y] in dot:
    print("%d %d"%(x,y))
