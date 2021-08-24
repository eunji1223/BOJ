import math
def judge(num):
    if num==1:
        return False
    if num==2:
        return True
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True

a_list=list(range(2,246912)) #제한에 유의
ss=[]
for i in a_list:
    if judge(i):
        ss.append(i)
while(True):
    ip=int(input())
    if ip==0:
        break
    count=0
    for j in ss:
        if ip<j<=(2*ip):
            count+=1
    print(count)

#시간 초과된 코드           
while(True):
    ip=int(input())
    if ip==0:break
    count=0
    for i in range(ip+1,(2*ip)+1):
        if i == 1:continue
        elif i==2:
            count+=1
            continue
        else:
            for j in range(2,int((math.sqrt(i))+1)):
                if i%j==0:break
            else:count+=1
    print(count)
        
