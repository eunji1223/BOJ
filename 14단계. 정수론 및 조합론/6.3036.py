num=int(input())
numlist=list(map(int,input().split()))
def GCD(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
for i in range(1,num):
    gcd=GCD(numlist[0],numlist[i])
    numer=numlist[0]//gcd
    denom=numlist[i]//gcd
    print(str(numer)+"/"+str(denom))
