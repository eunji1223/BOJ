A,B,C=map(int,input().split())
if B >= C: print("-1")
else:
    n = A/(C-B)
    n+=1
    print(n)
