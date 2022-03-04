n=int(input())
dp[0]*(n+1)
for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
print(dp[n])
"""
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


def one(N):
    return N-1
def two(N):
    if N%2==0:return N//2
    else:return None
def three(N):
    if N%3==0:return N//3
    else:return None
def repeat(N,count):
    
    if two(N)!=None:
N=int(input())
Nli=[]

"""
    
