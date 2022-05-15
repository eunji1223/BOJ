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
"""
melon = int(input()) # 참외 개수 K
values = [input().split() for _ in range(6)] # 나머지 2~7 line의 6 줄을 입력 받는다.
directions = [int(v[0]) for v in values] # 방향을 뽑아내서 저장한다.
lengths = [int(v[1]) for v in values] # 길이를 뽑아내서 저장한다.
max_lengths, box_lengths = [], [] # 큰 박스의 길이, 작은 박스의 길이를 담을 배열

for i in range(1, 5):
    if directions.count(i) == 1: # direction이 한번만 존재한다 == 큰 박스의 변
        max_lengths.append(lengths[directions.index(i)]) # 큰박스의 변 길이 저장
        temp = directions.index(i) + 3 # 큰 박스 + 3 == 작은 박스의 변
        if temp >= 6:
            temp -= 6 # cycle을 위해 6 이상일 경우 -6
        box_lengths.append(lengths[temp]) 

area = max_lengths[0] * max_lengths[1] - box_lengths[0] * box_lengths[1]
print(melon * area)
