import math
N,W,H=map(int,input().split())
for i in range(N):
    t=int(input())
    if t<=W or t<=H or t<=math.sqrt(W**2+H**2):
        print("DA")
    else:
        print("NE")
