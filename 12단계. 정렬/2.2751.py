import sys
input=sys.stdin.readline
ip=int(input())
number=[]
for i in range(ip):
    num=int(input())
    number.append(num)
number.sort()
for k in number:
    print(k)
