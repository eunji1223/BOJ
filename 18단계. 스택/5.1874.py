n=int(input())
curr=1
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
