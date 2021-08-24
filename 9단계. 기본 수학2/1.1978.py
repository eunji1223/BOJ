ip=int(input())
nums=list(map(int,input().split()))
count=0
for i in nums:
    result=True
    if i==1:result=False
    for j in range(2,i):
        if i%j==0:result=False
    if result==True:count+=1
print(count)
        
        
