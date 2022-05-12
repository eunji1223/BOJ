num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = num1*num2*num3
num_s = [0]*10
print(num_s)
while sum != 0:
    num = sum%10
    sum = sum//10
    num_s[num]+=1
for i in num_s:
    print(i)
    
