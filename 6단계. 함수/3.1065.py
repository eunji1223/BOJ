a = int(input())
count = 0
for i in range(1,a+1):
    if i<100:count+=1
    else:
        n1=i//100
        n2=(i%100)//10
        n3=(i%10)
        if (n1-n2)==(n2-n3) or (n3-n2)==(n2-n1):
            count+=1
print(count)
