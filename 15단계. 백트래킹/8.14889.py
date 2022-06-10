import sys
input = sys.stdin.readline

n=int(input())
visited = [false for _ in range(n)]
graph = [list(map(int,input().split()) for _ in range(n)]
mins=99999999

def Ability(depth,index):
    global min
    if depth==n//2:
        start=[]
        link=[]
        for i in range(len(visited)):
            if visited[i]==True:
                start.append(visited[i])
            else: link.append(visited[i])
        startS=0
        linkS=0
        for i in range(len(start)):
            for j in range(len(start)):
                if(start[i]==start[j]): continue
                startS=graph[start[i]][start[j]]
        for j in range(len(link)):
            for j in range(len(link)):
                if link[i]==link[j]: continue
                linkS=graph[link[i]][link[j]]
        mins=min(mins,abs(startS-linkS))
        return
idx=0
for i in range(idx,n):
    if not visited[i]:
        visited[i]=True
        Ability(depth+1,i+1)
        visited[i]=False
