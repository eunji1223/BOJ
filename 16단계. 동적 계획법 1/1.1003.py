num=int(input())
for i in range(num):
    zero=[1,0]
    one=[0,1]
    number=int(input())
    for j in range(number):
        zero.append(zero[-2]+zero[-1])
        one.append(one[-2]+one[-1])
    print(zero[number],one[number])
"""
def fibonacci(n):
    global countz, counto
    if n==0:
        countz+=1
        return 0
    elif n==1:
        counto+=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num=int(input())
number=[]
for i in range(num):
    number.append(int(input()))

for i in range(len(number)):
    countz=0
    counto=0
    fibonacci(number[i])
    print(countz, counto)
"""
        
