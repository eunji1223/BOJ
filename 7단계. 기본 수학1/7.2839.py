ip=int(input())
count=0
if ip//5!=0 and (ip%5)%3==0:
    count+= (ip//5)+(ip%5//3)
elif ip//5!=0 and (ip-(((ip//5)-1)*5))%3==0:
    count+=((ip//5)-1)+((ip-(((ip//5)-1)*5))//3)
elif ip//3!=0 and ip%3==0:
    count+=ip//3
else:
    count=-1
print(count)


ip=int(input())
count=0
while ip>=0:
    if ip%5==0:
        count+=ip//5
        break
    ip-=3
    count+=1
if ip<0:print(-1)
else:print(count)
