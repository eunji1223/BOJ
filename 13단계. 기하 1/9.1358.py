W,H,X,Y,P=map(int,input().split())
radi = H/2
count = 0
for i in range(P):
    x,y=map(int,input().split())
    if X<=x and x<=X+W and Y<=y and y<=Y+H:
        count+=1
    elif (Math.pow((X-x),2) + Math.pow((Y+radi-y),2))<Math.pow(radi,2):
        count+=1
    elif (Math.pow((X+W-x),2) + Math.pow((Y+radi-y),2))<Math.pow(radi,2):
        count+=1
print(count)
