N,M=map(int,input().split())
num=[0]+list(map(int,input().split()))
for i in range(1,len(num)):
    num[i]+=num[i-1]
print(num)
for j in range(M):
    a,b=map(int,input().split())
    if b-a<1:
        print(num[b]-num[b-1])
    else:
        print(num[b]-num[a-1])
