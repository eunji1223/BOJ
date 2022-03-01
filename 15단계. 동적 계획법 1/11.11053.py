LIS=[1] #가장 긴 증가하는 부분 수열
for i in range(1,n):
    LIS[i]=1
    for j in range(i-1,-1,-1):
        
