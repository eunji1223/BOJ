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
    print(i)
    Psum[i][ord(S[i])-97]=1
    for j in range(26):
        Psum[i][j]+=Psum[i-1][j]

for i in range(q):
    s,l,r=input().split()
    if int(l)>0:
        result = Psum[int(r)][ord(s)-97]-Psum[int(l)-1][ord(s)-97]
    else:
        result=Psum[int(r)][ord(s)-97]
    print(result)
    
