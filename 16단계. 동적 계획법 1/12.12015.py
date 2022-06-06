#입력 데이터 1000000개 --> 시간 제한 1초로 O(nlogn)이하의 방법으로 접근해야 함
#A[0]~A[n]까지 순회함으로 O(n)시간이 소요 따라서 D[k]중 큰 값을 O(logn)으로 찾아야 함

N=int(input())
A=list(map(int,input().split()))
D=[0]
for i in range(N):
    low=0
    high=len(D)-1
    while low<=high:
        mid=(low+high)//2
        if D[mid]<A[i]:low=mid+1
        else: high=mid-1
    if low>=len(D):D.append(A[i])
    else: D[low]=A[i]
print(len(D)-1)

