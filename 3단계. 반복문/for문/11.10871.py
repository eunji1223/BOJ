sum,num = map(int,input().split())
set = input().split()
num_arr = []
for i in set:
    if int(i)<num:
        num_arr.append(i)
for i in num_arr:
    print(i,end=' ')
