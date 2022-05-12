result=""
N=int(input())
NL=list(map(int,input().split()))
M=int(input())
ML=list(map(int,input().split()))
Ints=set(NL)&set(ML)
for i in ML:
    if i in Ints:result+="1"
    else: result+="0"
    result+=" "
print(result)
    
