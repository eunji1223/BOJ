num=int(input())
numlist=list(map(int,input().split()))
maxnum=max(numlist)
minnum=min(numlist)
print(maxnum*minnum)
#가장 작은값, 큰 값 곱한 수가 원래 수 임을 이용
"""
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)

num=int(input())
numlist=list(map(int,input().split()))

if num==1:
    print(numlist[0]*numlist[0])
elif num==2:
    print(numlist[0]*numlist[1])
else:
    while(len(numlist)>1):
        a=numlist.pop()
        b=numlist.pop()
        c=lcm(a,b)
        numlist.append(c)
    print(numlist[0])
"""#최대공약수, 최소공배수 이용함 --> 틀렸습니다라 나
