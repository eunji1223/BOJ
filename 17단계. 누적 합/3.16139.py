import sys
input=sys.stdin.readline

S=input().strip() # strip() : 공백 제거
q=int(input())
Psum=[[0 for i in range(26)] for i in range(len(S))]
"""만약 a라면 s e u n g j a e h w a n g
              0 0 0 0 0 0 1 1 1 1 2 2 2
        b라면 0 0 0 0 0 0 0 0 0 0 0 0 0
   문장의 길이만큼 26개 알파벳에 들어가는 갯수만큼의 리스트를 만
"""

Psum[0][ord(S[0])-97]=1
for i in range(1,len(S)):
    Psum[i][ord(S[i])-97]=1
    for j in range(26): # 이전의 값을 더해줌
        Psum[i][j]+=Psum[i-1][j]

for i in range(q):
    s,l,r=input().split()
    if int(l)>0: # 0보다 큰 경우
        result = Psum[int(r)][ord(s)-97]-Psum[int(l)-1][ord(s)-97]
        # r - l까지의 l,r을 포함한 미리 구한 값으로 구간에 위치한 알파벳 값 구함
    else:
        result=Psum[int(r)][ord(s)-97] # 0부터라 r까지의 값을 구함
    print(result)
    
