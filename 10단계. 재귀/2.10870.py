ip=int(input())
num=0
num1=num2=1
if ip==0:
    num2=0
for i in range(2,ip+1):
    num2=num+num1
    num=num1
    num1=num2
print(num2)

def fibonacci(num):
    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

n=int(input())
print(fibonacci(n))
