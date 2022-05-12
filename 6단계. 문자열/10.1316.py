num=int(input())
s_short=[]
error=0
for i in range(num):
    seq=input()
    s_short=list(''.join(dict.fromkeys(seq)))
    result=True
    for k in range(len(seq)-1):
        if seq[k]!=seq[k+1]:
            if seq[k] not in s_short:
                result=False
                break
            s_short.remove(seq[k])
        if seq[len(seq)-1] not in s_short:
            result=False
    if result==False:
        error+=1      
print(num-error)
        
