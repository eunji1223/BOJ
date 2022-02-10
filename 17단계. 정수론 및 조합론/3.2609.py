#유클리드 호제법
a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b #a = a%b, a,b = b,a
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))
"""
a,b=map(int,input().split())
if a>b:
    temp=a
    a=b
    b=temp
max=0
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        max=i
min=b+i
while(True):
    if min%a==0 and min%b==0:
        break
    min+=i
print(i)
print(min)
"""
    
        
    
