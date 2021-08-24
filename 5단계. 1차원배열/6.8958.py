test = int(input())
for i in range(test):
    people = 0
    num_sco = list(map(int,input().split()))
    num = num_sco[0]
    num_sco[0] = 0
    avg = sum(num_sco,0.0)/num
    for n in num_sco:
        if n > avg:
            people += 1
    print("%.3f"%(people/num*100)+"%")
