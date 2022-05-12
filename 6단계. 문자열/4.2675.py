test = int(input())
for i in range(test):
    num,sent = input().split()
    for j in sent:
        for k in range(int(num)):
            print(j,end='')
    print("")
