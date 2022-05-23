"""
import math
W,H,X,Y,P=map(int,input().split())
radi = H/2
count = 0
for i in range(P):
    x,y=map(int,input().split())
    if X<=x and x<=X+W and Y<=y and y<=Y+H:
        count+=1
    elif (math.pow((X-x),2) + math.pow((Y+radi-y),2))<math.pow(radi,2):
        count+=1
    elif (math.pow((X+W-x),2) + math.pow((Y+radi-y),2))<math.pow(radi,2):
        count+=1
print(count)

"""

W,H,X,Y,P=map(int,input().split())
count=0
for i in range(P):
    x,y=map(int,input().split())

    if ((x-X)*(x-X)+(y-(Y+H/2))*(y-(Y+H/2))<=(H/2)*(H/2) and x<X):
            count+=1
    elif (X<=x and x<=X+W and Y<=y and y<=Y+H):
        count+=1
    elif ((x-(X+W))*(x-(W+X))+(y-(Y+H/2))*(y-(Y+H/2))<=(H/2)*(H/2) and X+W<x):
        count+=1
print(count)
