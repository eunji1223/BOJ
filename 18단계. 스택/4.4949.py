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
        
    
    
