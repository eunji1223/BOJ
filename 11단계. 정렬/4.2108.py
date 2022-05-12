#산술평균, 중앙값, 최빈값, 범위

#메모리 초과 되었었음

import collections
import sys
input=sys.stdin.readline
numbers=[]
sum=0
for i in range(int(input())):
    num=int(input())
    numbers.append(num)
    sum+=num
numbers.sort()
count=collections.Counter(numbers).most_common() #함수 이용
print(round(sum/len(numbers)))
print(numbers[len(numbers)//2])
if len(numbers)>1:
    if count[0][1]==count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
print(numbers[-1]-numbers[0])

#시간 초과
'''
import sys
input=sys.stdin.readline
test=int(input())
number=[]
sum=0
for i in range(test):
    num=int(input())
    number.append(num)
    sum+=num
number.sort()
setnumber=list(set(number))
count=[0]*len(setnumber)
for j in number:
    count[setnumber.index(j)]+=1
counum=count.count(max(count))
if counum>1 and max(count)!=1:
    setnumber.pop(count.index(max(count)))
    count.pop(count.index(max(count)))
freq=count.index(max(count))
print(round(sum/len(number)))
print(number[len(number)//2])
print(setnumber[freq])
print(number[-1]-number[0])
'''    
