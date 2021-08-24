sentence = input().upper()
word = list(set(sentence))
num = [0]*len(word)
for i in word:
    num[word.index(i)]=sentence.count(i)
max = max(num)
max_list = []
for i in range(len(num)):
    if num[i]==max:
        max_list.append(i)
if len(max_list)==1:
    print(word[max_list[0]])
else:
    print("?")

