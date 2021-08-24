import sys
sys.setrecursionlimit(10**6)

def star(num):
    if num==1:
        return['*']

    star_num=star(num//3)
    L=[]
    for i in star_num:
        L.append(i*3)
    for j in star_num:
        L.append(j+' '*(num//3)+j)
    for k in star_num:
        L.append(k*3)
    return L

n=int(sys.stdin.readline().strip())
print('\n'.join(star(n)))

#--------------------------------------------------------------------
#분할 정복 알고리즘 이용
def stars(num): #star list 입력
    maps=[]
    for i in range(3*len(num)): 
        if i//len(num)==1:
            maps.append(num[i%len(num)]+" "*len(num)+num[i%len(num)])
        else:
            maps.append(num[i%len(num)]*3)
    return(list(maps))
star=["***","* *","***"]
n=int(input())
k=0
while n!=3:
    n=int(n/3)
    k+=1
for i in range(k):
    star=stars(star)
for i in star:
    print(i)


