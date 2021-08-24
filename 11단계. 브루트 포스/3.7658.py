import sys
input=sys.stdin.readline
test=int(input())
form=[]
for i in range(test):
    H=list(map(int,input().split()))
    form.append(H)
for j in form:
    count=1
    for k in form:
        if j[0]<k[0] and j[1]<k[1]:
            count+=1
    print(count,end=' ')

#-----------------------------------------------------------
'''
import sys
input=sys.stdin.readline
test=int(input())
form=[]
for i in range(test):
    H=list(map(int,input().split()))
    form.append(H)
result=sorted(form)
count=1
score=[]
for j in range(len(result)-1,-1,-1):
    if result[j][1]>result[j-1][1]:
        if j==0:
            last = score[len(score)-1] + score.count(score[len(score)-1])
            score.append(last)
        else:score.append(count)
    elif result[j][1]<=result[j-1][1]:
        if j==0:
            last = score[len(score)-1] + score.count(score[len(score)-1])
            score.append(last)
        else:
            score.append(count)
            continue
    count+=1
for x in form:
    a=result.index(x)
    print(score[test-1-a],end=' ')
'''
