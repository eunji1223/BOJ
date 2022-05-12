ip=int(input())
for i in range(ip):
    x,y=map(int,input().split())
    diff=y-x
    number=1
    while(True):
        if number**2<=diff<(number+1)**2:
            break
        number+=1
    if number**2==diff:
        print((number*2)-1)
    elif number**2<diff<=number**2+number:
        print(number*2)
    else:
        print(number*2+1)
