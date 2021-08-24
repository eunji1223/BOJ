num_s = [0]*42
for i in range(10):
    num = int(input())
    if num_s[num%42] == 0:
        num_s[num%42] += 1
sum = 0
for i in num_s:
    sum += i
print(sum)
    
