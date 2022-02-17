"""
case=int(input())
for i in range(case):
    num=int(input())
    wearlist=[]
    wearlistc=[]
    for j in range(num):
        name=list(input().split())
        if name[-1] in wearlist:
            wearlistc[wearlist.index(name[-1])]+=1
        else:
            wearlist.append(name[-1])
            wearlistc.append(1)
    count=1
    for k in range(len(wearlistc)):
        count*=wearlistc[k]
    if len(wearlistc)==1:
        print(count)
    else:
        print(count+num)
"""

from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)
        
            
        
