dice=list(map(int,input().split()))
s=0 #갯수
sn=0 #숫
for i in range(3):
    count=0
    for j in range(3):
        if dice[i]==dice[j]:
            count+=1
    if count>s:
        s=count
        sn=dice[i]
if s==3:
    print(10000+sn*1000)
elif s==2:
    print(1000+sn*100)
elif s==1:
    print(max(dice)*100)
            
