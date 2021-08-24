import sys
input=sys.stdin.readline
test=int(input())
class Stack:
    def __init__(self):
        self.A=[]
    def push(self,num):
        self.A.append(num)
    def pop(self):
        if self.size():
            return self.A.pop()
        else:
            return -1
    def top(self):
        if self.size():
            return self.A[-1]
        else:
            return -1
    def size(self):
        leng=len(self.A)
        return leng
    def empty(self):
        a=self.size()
        if a:return 0
        else:return 1

A=Stack()    
for i in range(test):
    order=list(input().split())
    if order[0]=='push':
        A.push(order[1])
    elif order[0]=='pop':
        print(A.pop())
    elif order[0]=='top':
        print(A.top())
    elif order[0]=='size':
        print(A.size())
    elif order[0]=='empty':
        print(A.empty())
