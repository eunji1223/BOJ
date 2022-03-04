def find(N,count):
    if N==1:
        print(count)
        return
    if N%3==0:
        find(N//3,count+1)
    elif N%2==0:
        find(N//2,count+1)
    else:
        find(N-1,count+1)

N=int(input())
result=find(N,0)
