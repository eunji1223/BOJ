M=int(input())
N=int(input())
s_list=[]
for i in range(M,N+1):
    result=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                result=1
                break
        if result==0:
            s_list.append(i)
if len(s_list)>0:
    print(sum(s_list))
    print(min(s_list))
else:
    print(-1)
