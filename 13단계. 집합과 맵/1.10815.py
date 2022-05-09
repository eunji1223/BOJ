result=""
N=int(input())
NL=set(list(map(int,input().split())))
M=int(input())
ML=set(list(map(int,input().split())))
Ints=NL.intersection(ML)
for i in NL:
    if i in Ints:result+="1"
    else: result+="0"
    result+=" "
print(result)
    
