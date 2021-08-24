num = int(input())
sco = list(map(int,input().split()))
big = max(sco)
for i in range(num):
    sco[i] = sco[i]/big*100
avg = sum(sco,0.0)/len(sco)
print(avg)
