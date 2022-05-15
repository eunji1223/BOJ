""" #런타임 에러
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
"""
k=int(input())
NL=[list(map(int,input().split())) for _ in range(k-1)]
Br=0
Bc=0
ridx=0
cidx=0
for i in range(len(NL)):
    print(NL[i][0])
    if NL[i][0]==1 or NL[i][0]==2:
        if Br<NL[i][1]:
            Br=NL[i][1]
            ridx=i
    elif NL[i][0]==3 or NL[i][0]==4:
        if Bc<NL[i][1]:
            Bc=NL[i][1]
            cidx=i
sr=abs(NL[(ridx-1)%6][1]-NL[(ridx+1)%6][1])
sc=abs(NL[(cidx-1)%6][1]-NL[(cidx+1)%6][1])
print(Br,Bc,sr,sc)
result=((Br*Bc)-(sr*sc))*7
print(result)
#가장 긴 가로변 양옆에 붙어있는 변(세로변)들의 차이 : 뺄 사각형의 세로
#가장 긴 세로변 양옆에 붙어있는 변(가로변)들의 차이 : 뺄 사각형의 가로
        
