N,M=map(int,input().split())
board=list()
for i in range(N):
    board.append(input())
repair=list()

for i in range(N-7):
    for j in range(M-7):
        first_W=0
        first_B=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if(k+l)%2==0:
                    if board[k][l]!='W':
                        first_W+=1
                    if board[k][l]!='B':
                        first_B+=1
                else:
                    if board[k][l]!='B':
                        first_W+=1
                    if board[k][l]!='W':
                        first_B+=1
        repair.append(first_W)
        repair.append(first_B)
print(min(repair))
"""
N,M=map(int,input().split())
chess=[] #체스판
first=[] #첫 시작
count=0
for i in range(N):
    A=input()
    chess.append(A)
    first.append(A[0])
for j in range(len(chess)-1):
    for k in range(len(chess[j])-1):
        if k%2==0:
            if chess[j][k]==first[j]:continue
            else:count+=1
        else:
            if chess[j][k]!=first[j]:continue
            else:count+=1
print(count)
"""
        
