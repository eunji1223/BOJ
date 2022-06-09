import sys
input = sys.stdin.readline

N=int(input())
SN=list(map(int,input().split()))

M=int(input())
NM=list(map(int,input().split()))
count=[0 for _ in range(M)]
ints=list(set(SN)&set(NM))
for i in range(len(ints)):
    idx=NM.index(ints[i])
    count[idx]+=1
print(*count)
