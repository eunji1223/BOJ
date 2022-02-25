def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return 1048576
    elif a<b and b<c:
        return w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    else:
        return w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)

a,b,c=map(int,input().split())
while(a!=-1 or b!=-1 or c!=-1):
    print(w(a,b,c))
    a,b,c=map(int,input().split())
