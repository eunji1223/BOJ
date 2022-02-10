num=int(input())
numlist=[]
for i in range(num):
    a=int(input())
    if a==0:
        numlist.pop()
    else:
        numlist.append(a)
print(sum(numlist))
