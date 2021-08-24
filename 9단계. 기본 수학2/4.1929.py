M,N=map(int,input().split())
judge=[True]*(N+1)
for i in range(1,N+1):
    if i==1:
        judge[i]=False
        continue
    if judge[i]==False:
        continue
    for j in range(i+i,N+1,i):
        judge[j]=False
for k in range(len(judge)):
    if k>=M:
        if judge[k]==True:
            print(k)
