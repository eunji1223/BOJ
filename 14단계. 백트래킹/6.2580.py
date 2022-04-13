sdk=[list(map(int,input().split())) for _ in range(9)]
zero_loc=[(i,j) for i in range(9) for j in range(9) if sdk[i][j]==0]

def findN(y,x):
    number=[i+1 for i in range(9)]
    for i in range(9):
        if sdk[y][i] in number:
            number.remove(sdk[y][i])
        if sdk[i][x] in number:
            number.remove(sdk[i][x])
    y=y//3
    x=x//3
    for i in range(y*3,(y+1)*3):
        for j in range(x*3,(x+1)*3):
            if sdk[i][j] in number:
                numbers.remove(board[i][j])
    return number

result=False
def solve(count):
    global result
    if result: return
    if x==len(zeros):
        for row in sdk:
            print(*row)
        flag=True
        return
    else:
        (i,j)=zero_loc[x]
        N=findN(i,j)

        for num in N:
            sdk[i][j]=num
            solve(x+1)
            sdk[i][j]=0
solve(0)
    
