import sys

sdk=[list(map(int,input().split())) for _ in range(9)]
zero_loc=[(i,j) for i in range(9) for j in range(9) if sdk[i][j]==0] #zero 위치를 저장
def findN(r,c): # 각 위치에 대해 가능한 수를 확인 후 그 수 저장
    number=set(range(1,10))
    number-=set(sdk[r])
    test=set()
    for i in range(9):
        test.add(sdk[i][c])
    number-=test
    test=set()
    for i in range(r//3*3,r//3*3+3):
        for j in range(c//3*3,c//3*3+3):
            test.add(sdk[i][j])
    number-=test
    return tuple(number)

def solve(i):
    if i==len(zero_loc): #만약 모든 칸이 채워지면 출
        [print(*row) for row in sdk]
        sys.exit()
    r,c=zero_loc[i]
    number=findN(r,c)
    for num in number:
        sdk[r][c]=num
        solve(i+1)
        sdk[r][c]=0
solve(0)


""" #런타임에러 발생(pypy로 제출했음에도 불구하고 오랜 시간 소요)
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
    if count==len(zero_loc):
        for row in sdk:
            print(*row)
        flag=True
        return
    else:
        (i,j)=zero_loc[count]
        N=findN(i,j)

        for num in N:
            sdk[i][j]=num
            solve(count+1)
            sdk[i][j]=0
solve(0)
    
"""
