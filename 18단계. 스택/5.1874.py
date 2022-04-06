"""
n=int(input()) #입력 받을 갯수
curr=0 #현재 입력(수)
stack,ans=[],[]
X=True

for i in range(n):
    N=int(input())
    
    while curr<N: #현재 수가 입력받은 수와 같아질 때까지
        stack.append(curr) #스택에 숫자를 넣음
        ans.append('+') #숫자 추가됨
        curr+=1
    if stack[-1]==N: #마지막 값과 같을 경우
        ans.append('-') #숫자 감소됨
        stack.pop() #스택에서 숫자를 뺌
    else:
        X=False
        break
if X==False:
    print('No')
else:
    for i in ans:
        print(i)
"""
n=int(input())
stack=[]
result=[]
count=0
X=True

for i in range(n):
    num=int(input())
    while count<num:
        count+=1
        stack.append(count)
        result.append("+")
    if stack[-1]==num:
        stack.pop()
        result.append("-")
    else:
        X=False
        break
if X==False:
    print("NO")
else:
    for i in result:
        print(i)

