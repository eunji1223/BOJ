pro = big = 0
for i in range(9):
    num = int(input())
    if num > big :
        big = num
        pro = i
print(big)
print(pro+1)
