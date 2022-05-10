AN,BN=map(int,input().split())
A=set(list(map(int,input().split())))
B=set(list(map(int,input().split())))
AmB=A^B
BmA=B^A
print(len(AmB)+len(BmA))
