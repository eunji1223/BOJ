'''
test=int(input())
word=[]
word_len=[]
for i in range(test):
    ip=input()
    if ip in word:
        continue
    word.append(ip)
    word_len.append(len(ip))
result=[]
while len(result)!=len(word):
    minlen=min(word_len)
    locate=list(filter(lambda x:word_len[x]==minlen,range(len(word_len))))
    for j in locate:
        result.append(word[j])
print(result)
'''
#--------------------------------------------------
words_num = int(input())
words_list = []

for _ in range(words_num):
    word = str(input())
    word_count = len(word)
    words_list.append((word, word_count))

#중복 삭제
words_list = list(set(words_list))

#단어 숫자 정렬 -> 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))

for word in words_list:
    print(word[0])

#--------------------------------------------------
import sys #속도 줄어듬

n = int(sys.stdin.readline()) 
word = []

for i in range(n):
    word.append(sys.stdin.readline().strip())
word = list(set(word))
word.sort()
word.sort(key = len)

for j in word:
    print(j)
    
    


    
