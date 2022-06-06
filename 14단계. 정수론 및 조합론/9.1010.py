import math
num=int(input())
for i in range(num):
    N,M=map(int,input().split())
    result=math.factorial(M)//(math.factorial(N)*math.factorial(M-N))
    print(result)
#조합 이용
