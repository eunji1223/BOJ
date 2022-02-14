time,minutes=map(int,input().split())
plus=int(input())
ntime=time
nminutes=minutes+plus
while nminutes>=60:
    nminutes-=60
    ntime=ntime+1
    if ntime>23:
        ntime=0
print(ntime,nminutes)
    
    
