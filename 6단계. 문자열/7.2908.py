num=list(input().split())
renum=[]
for i in range(len(num)):
    a = int(num[i])
    b = ((a%10)*100)+(((a//10)%10)*10)+(a//100)
    renum.append(b)
print(max(renum))
