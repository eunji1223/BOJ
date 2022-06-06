"""
S=input()
while S!='.':
    SL=S.replace(" ","")
    sum1=0
    sum2=0
    for i in SL:
        if i=='(': sum1+=1
        elif i=='[': sum2+=1
        elif i==')': sum1-=1
        elif i==']': sum2-=1
        if sum1<0 or sum2<0:
            break
    if sum1==0 and sum2==0:print('yes')
    else: print('no')
    S=input()
"""

S=input()
while S!='.':
    stack=[]
    for i in S:
        if i in '([':
            stack.append(i)
        elif i==']':
            if not stack or stack.pop()!='[':
                print('no')
                break
        elif i==')':
            if not stack or stack.pop()!='(':
                print('no')
                break
        elif i=='.':
            if stack: print('no')
            else: print('yes')
    S=input()
    
        
    
    
