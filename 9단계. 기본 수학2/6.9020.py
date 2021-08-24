import math
def judge(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True

test=int(input())
for i in range(test):
    ip=int(input())
    if ip%2==0:
        if judge(ip//2)==True:
            print("%d %d"%(ip//2,ip//2))
        else:
            ip=ip//2
            count=1
            while True:
                if judge(ip-count)==True and judge(ip+count)==True:
                    print("%d %d"%(ip-count,ip+count))
                    break
                else:
                    count+=1
                    
                
                
        
        
