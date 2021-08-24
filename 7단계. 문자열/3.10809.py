sent = input()
s = [-1]*26
for i in range(len(sent)):
    if s[ord(sent[i])-97]==-1:
        s[ord(sent[i])-97]=i
for j in s:
    print(j,end=' ')
