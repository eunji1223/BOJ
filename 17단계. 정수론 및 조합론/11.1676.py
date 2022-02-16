num=int(input())
snum=1
for i in range(2,num+1):
    snum*=i
strnum=str(snum)
count=0
for j in range(len(strnum)-1,-1,-1):
    if int(strnum[j])!=0:
        break
    count+=1
print(count)
