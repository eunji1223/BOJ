n=int(input())
tri=[]
for i in range(n):
    tri.append(list(map(int,input().split())))
for i in range(1,len(tri)):
    tri[i][0]+=tri[i-1][0]
    for j in range(1,len(tri[i])-1):
        tri[i][j]+=max(tri[i-1][j-1],tri[i-1][j])
    tri[i][len(tri[i])-1]+=tri[i-1][len(tri[i-1])-1]
print(max(tri[len(tri)-1]))
