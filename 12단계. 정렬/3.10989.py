import sys
input=sys.stdin.readline
N = int(input())
check_list = [0] * 10001
for i in range(N):
    input_num = int(input())
    check_list[input_num] += 1
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)
            
''' 카운팅 정렬 공부 후 다시 하기
ip=int(input())
num_arr=[]
for i in range(ip):
    num=int(input())
    num_arr.append(num)
count=[0]*1000
for j in range(0,len(num_arr)):
    count[num_arr[j]]+=1
cSum=[0]*1000
cSum[0]=count[0]
for k in range(1,1000):
    cSum[k]=cSum[k-1]+count[i]

B=[0]*(ip+1)
for a in range(ip-1,-1,-1):
    B[cSum[num_arr[a]]] = num_arr[a]
    cSum[num_arr[a]]-=1

for b in range(1,1001):
    print(B[b])
'''

