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
        
