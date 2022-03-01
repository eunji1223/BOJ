numlist=[1,1,1]
def find(num):
    if len(numlist)<num:
        print(numlist)
        return numlist[num]
    else:
        numlist.append(numlist[num-2]+numlist[num-3])

T=int(input())
for i in range(T):
    num=int(input())
    print(find(num))

    
