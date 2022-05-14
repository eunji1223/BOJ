k=int(input())
NL=[]
Br=Bc=ridx=cidx=0
for i in range(k):
    n,l=map(int,input().split())
    if i%2==0:
        if l>Br:
            Br=l
            ridx=i
    else:
        if l>Bc:
            Bc=l
            cidx=0
    NL.append(l)
print(7*(Br*Bc-NL[ridx+3]*NL[cidx+3]))
