numlist=[1,1,1]
def find(count,num):
    if count>=num:
        return numlist[num-1]
    else:
        numlist.append(numlist[count-2]+numlist[count-3])
        find(count+1,num)

T=int(input())
for i in range(T):
    num=int(input())
    find(len(numlist),num)
    print(numlist[num-1])


    
