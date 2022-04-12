sdk=[list(map(int,input().split())) for _ in range(9]
zero_loc=[(i,j) for i in range(9) for j in range(9) if board[i][j]==0]

def solve(y,x):
    number=[i+1 for i in range(9)]
    for i in range(9):
        if sdk[y][i] in number:
            number.remove(sdk[y][i])
        if sdk[i][x] in number:
            number.remove(sdk[i][x])
    
