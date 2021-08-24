ip=int(input())
number=list(map(int,input().split()))
num=sorted(list(set(number)))
count={num[i]: i for i in range(len(num))}
for j in number:
    print(count[j],end=' ')
