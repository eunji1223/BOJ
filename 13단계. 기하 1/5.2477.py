k=int(input())
NL=[]
Br=Bc=ridx=cidx=0
for i in range(1,k):
    n,l=map(int,input().split())
    if i%2==0:
        if l>Br:
            Br=l
            ridx=i
            print("실행")
    else:
        if l>Bc:
            Bc=l
            cidx=0
    NL.append(l)
print(ridx,cidx)
result=Br*Bc-NL[ridx+3]*NL[cidx+3]
print(7*result)
