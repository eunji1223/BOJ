listN=[]
str=input()
for i in range(1,len(str)+1):
    start=0
    while(start+i<=len(str)):
        listN.append(str[start:start+i])
        start+=1
listN=set(listN)
print(len(listN))
