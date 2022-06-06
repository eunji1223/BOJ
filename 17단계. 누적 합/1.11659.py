"""
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
num=[0]+list(map(int,input().split()))
for i in range(1,len(num)):
    num[i]+=num[i-1]
print(num)
for j in range(M):
    a,b=map(int,input().split())
    if b-a<1:
        print(num[b]-num[b-1])
    else:
        print(num[b]-num[a-1])
""" #--> 어째서 출력초과..
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
num=list(map(int,input().split()))
prefix_sum=[0]

temp=0
for i in num:
    temp+=i
    prefix_sum.append(temp)
for j in range(M):
    a,b=map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])
