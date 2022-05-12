CAlphabet = ['č','ć','dž','đ','lj','nj','š','ž']
Change = ['c=','c-','dz=','d-','lj','nj','s=','z=']
ip = input()
count = 0
for i in range(len(Change)):
    if Change[i] in ip:
        count+=ip.count(Change[i])
        ip = ip.replace(Change[i]," ")
ip=ip.replace(" ","")
print(count+len(ip))
