movelist=[]

def move(n,A,B,C):
    if n==0:return
    move(n-1,A,C,B)
    movelist.append(str(A)+" "+str(C))
    move(n-1,B,A,C)

n=int(input())
move(n,1,2,3)
print(len(movelist))
for i in range(len(movelist)):
    print(movelist[i])
