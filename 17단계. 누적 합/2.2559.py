"""
import sys
input = sys.stdin.readline
N,K=map(int,input().split())
num=list(map(int,input().split()))
max=0
numS=[0]
for i in range(1,N):
    numS.append(numS[i-1]+num[i])
for i in range(N-K):
    if numS[i+K]-numS[i]>max:
        max=numS[i+K]-numS[i]
print(max)
""" # 틀린 결과가 있다고 표시됨

N, K = map(int, input().split())
tem_list = list(map(int, input().split()))

part_sum = sum(tem_list[:K]) # 미리 구간의 범위를 구함(초반)
result_list = [part_sum]

for i in range(0, len(tem_list)-K):
    part_sum = part_sum - tem_list[i] + tem_list[i+K]
    # 구간의 크기를 유지하면서 앞의 값은 빼고 다음 값은 더
    result_list.append(part_sum)

print(max(result_list))

""" # --> 최
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = list(map(int, input().split()))

middle = sum(num[:K])
result = [middle]

for i in range(0, N-K):
    middle = middle - num[i] + num[i+K]
    result.append(middle)

print(max(result))
"""
