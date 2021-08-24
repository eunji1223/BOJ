import sys
input=sys.stdin.readline #시간 초과가 뜨기 때문에 추가
test=int(input())
dot=[]
for i in range(test):
    [x,y]=map(int,input().split())
    dot.append([y,x])
result=sorted(dot)
for i in range(test):
    print(result[i][1],result[i][0])


#시간 초과 #런타임 에러 +(import sys 추가 시)
'''
test=int(input())
dot=[]
for i in range(test):
    x,y=map(int,input().split())
    dot.append([y,x])
dot=sort()
for [y,x] in dot:
    print("%d %d"%(x,y))
'''
