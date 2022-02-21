"""
num=int(input())
nlist=[]
for i in range(num):
    nlist.append(int(input()))
minn=min(nlist)
save=[]
for i in range(2,minn):
    first=nlist[0]%i
    result=True
    for j in range(1,num):
        if (nlist[j]%i)!=first:
            result=False
            break
    if result==True:
        save.append(i)

for i in range(len(save)):
    print(save[i], end=' ')

"""
#for 범위min이면 2 5일 경우 아무것도 안나옴, 3이 나와야 함
#for 범위max이면 시간초과가 남

import math

num = int(input())
nlist = []
result = []
for i in range(num):
    nlist.append(int(input()))
nlist.sort()
temp = [nlist[i] - nlist[i - 1] for i in range(1, num)] #각 인접 요소들끼리 뺄셈
gcd = temp[0]

for i in range(1, num - 1):
    gcd = math.gcd(gcd, temp[i]) #--> 모든 요소 gcd구함

for i in range(1, int(math.pow(gcd, 1 / 2)) + 1):
    #math.pow --> 제곱근 반환 my_gcd의 1/2제곱근 반환
    if gcd % i == 0:
        if i ** 2 == gcd:
            result.append(i)
        else:
            result += [i, gcd // i]
result.remove(1)
result.sort()

for i in range(len(result)):
    print(result[i], end=" ")
