AN,BN=map(int,input().split())
A=set(list(map(int,input().split())))
B=set(list(map(int,input().split())))
AmB=A^B
print(len(AmB)) #차집합 -,difference / 대칭 차집합 ^
