num=int(input())
nlist=[]
for i in range(num):
    nlist.append(int(input()))
minn=min(nlist)
save=[]
for i in range(2,minn):
    first=nlist[0]%i
    result=True
    for j in range(1,num):
        if (nlist[j]%i)!=first:
            result=False
            break
    if result==True:
        save.append(i)

for i in range(len(save)):
    print(save[i], end=' ')
