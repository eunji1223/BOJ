"""
import sys
input = sys.stdin.readline

N=int(input())
SN=list(map(int,input().split()))

M=int(input())
NM=list(map(int,input().split()))
count=[0 for _ in range(M)]
ints=list(set(SN)&set(NM))
for i in range(len(ints)):
    c = SN.count(ints[i])
    idx=NM.index(ints[i])
    count[idx]=c
print(*count)

# 딕셔너리 이용
import sys
input = sys.stdin.readline

N=int(input())
SN=list(map(int,input().split()))

M=int(input())
NM=list(map(int,input().split()))

count={}
ints=list(set(SN)&set(NM))
for i in range(len(ints)):
    count[ints[i]]=SN.count(ints[i])
for i in range(len(NM)):
    if NM[i] in count.keys(): print(count[NM[i]], end=' ')
    else: print('0',end=' ')
""" # 시간 초과

import sys
input = sys.stdin.readline

N=int(input())
SN=list(map(int,input().split()))

M=int(input())
NM=list(map(int,input().split()))

count = {}
for n in SN:
    if n in count:count[n]+=1
    else:count[n]=1
for m in NM:
    result = count.get(m)
    if result == None: print(0, end=' ')
    else: print(result, end)
        


