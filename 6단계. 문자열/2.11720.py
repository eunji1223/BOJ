num = int(input())
s_num = input()
sum = count = 0
for i in str(s_num):
    sum+=int(i)
    count+=1
    if count > num:
        break
print(sum)
    
