ip = int(input())
count = 0
bnum =  1
while True:
    if ip <= bnum+(6*count):
        count+=1
        break
    bnum+=6*count
    count+=1
print(count)
    
