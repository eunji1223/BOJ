N=int(input())
num=[]

for i in range(1,N-1):
    sumN=[int(j) for j in str(i)]
    result=sum(sumN)
    if result+i==N:
        num.append(i)
if len(num)<1:
    print(0)
else:
    print(min(num))

