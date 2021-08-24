# 1  -  2  -  3  -  4  -  5  -  6  -  7  -  8
#1/1 - 1/2 - 2/1 - 3/1 - 2/2 - 1/3 - 1/4 - 2/3
# 1        2              3              4 ...
ip = int(input())
num=0
count=1
while ip>num:
    num+=count
    count+=1
diff=num-ip
if (count-1)%2==0:
    top=count-1-diff
    bottom=count-top
else:
    bottom=count-1-diff
    top=count-bottom
print("%d/%d"%(top,bottom))

