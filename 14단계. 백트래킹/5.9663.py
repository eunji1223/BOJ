def B(k,col):
    for i in range(1,k):
        if x[i]==col or abs(x[i]-col)==abs(i-k):
            return False
    return True

def NQueens(k):
    global sol
    if k>N:
        sol+=1
        return
    for col in range(1,N+1):
        x[k]=col
        if B(k,col):
            NQueens(k+1)

N=int(input())
x=[0]*(N+1)
sol=0
NQueens(1)
print(sol)
