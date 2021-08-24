num = int(input())
for i in range(num):
    s = input()
    score = 0
    s_score = 0
    for j in s:
        if j=='O': score += 1
        else: score = 0
        s_score += score
    print(s_score)
