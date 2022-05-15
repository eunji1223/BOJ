k=int(input())
NL=[]
Br=0
Bc=0
ridx=0
cidx=0
for i in range(1,k):
    n,l=map(int,input().split())
    if i%2==0:
        if l>Br:
            Br=l
            ridx=i
    else:
        if l>Bc:
            Bc=l
            cidx=i
    NL.append(l)
result=Br*Bc-NL[ridx+2]*NL[cidx+2]
print(7*result)
