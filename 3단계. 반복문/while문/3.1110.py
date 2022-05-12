num = int(input())
s_num = num
count = 0
while(True):
    sum = s_num//10 + s_num%10
    s_num = ((s_num%10)*10)+(sum%10)
    count += 1
    if num == s_num:break
print(count)
