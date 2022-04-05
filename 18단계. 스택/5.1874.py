n=int(input()) #입력 받을 갯수
curr=1 #현재 입력(수)
stack,ans=[],[]
for i in range(n):
    N=int(input())
    while curr<=N:
        stack.append(curr)
        ans.append('+')
        curr+=1
    if stack[-1]==N:
        ans.append('-')
        stack.pop()
if not stack:
    print('\n'.join(ans))
else:
    print('No')

