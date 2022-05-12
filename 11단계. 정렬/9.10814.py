test=int(input())
info=[]
ages=[]
for i in range(test):
    age,name=input().split()
    info.append((int(age),name))
    ages.append(int(age))

ages=list(set(ages))
ages.sort()
for j in ages:
    for (a,b) in info:
        if a==j:
            print(a,b)
