def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]: 
            print(seq[i], end="")
        else:
            print("_", end="")
    print()

def LIS_DP(seq):
	x=[0]*len(seq)
	DP=[0]*len(seq)
	for i in range(len(seq)): #앞의 경우와 비교해 증가 문자열의 최대길이 찾기, O(n)
		for j in range(i): #O(n)
			if seq[i]>seq[j]:DP[i]=max(DP[i],DP[j]+1)
	count=result=max(DP) #최대 길이 담기
	max_I=DP.index(result) # 최대 길이의 인덱스 찾기
	num=len(seq)-1
	while max_I>=0: #O(n), 리스트에 최대 문자 담기
		if DP[max_I]==result: 
			x[num]=seq[max_I]
			num-=1
			result-=1
		max_I-=1
	str=''
	for i in range(len(x)): #리스트를 문자열 형태로 바꾸기, O(n)
		if x[i]!=0:
			str+=x[i]
	return count+1,str

A = input()
B = input() #알파벳 대문자로만 구성된 A,B가 존재
lis, x = LIS_DP(A+" "+B)
print(lis)


