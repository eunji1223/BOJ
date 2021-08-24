x,y,w,h=map(int,input().split())
minlist=[]
minlist.append(w-x)
minlist.append(h-y)
minlist.append(x)
minlist.append(y)
print(min(minlist))

#-------------
#|           |
#|     .     |
#|           |
#|           |
#-------------

#또는 a=w-x --> min(a,b,c,d) 로 풀기 가능
