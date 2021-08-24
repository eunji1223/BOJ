ip=int(input())
for i in range(ip):
    k=int(input())
    n=int(input())
    people=[z for z in range(1,n+1)]
    for j in range(k):
        for h in range(1,n):
            people[h]+=people[h-1]
    print(people[-1])
#1층의 3호면 1+2+3=6
#2층의 3호면 1+3+6=10
#3층의 3호면 1+4+10=15

