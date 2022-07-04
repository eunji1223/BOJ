import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.items=[]
        self.front_index=0
    def push(self,val):
        self.items.append(val)
    def pop(self):
        if self.front_index==len(self.items):
            return -1
        else:
            x=self.items[self.front_index]
            self.front_index+=1
            return x
    def size(self):
        return len(self.items)-self.front_index
    def empty(self):
        num = self.size()
        if num!=0:
            return 0
        else: return 1
    def front(self):
        num = self.size()
        if num!=0:
            return self.items[self.front_index]
        else:
            return -1
    def back(self):
        num = self.size()
        if num!=0:
            return self.items[len(self.items)-1]
        else:
            return -1

N=int(input())
Q=Queue()
for i in range(N):
    order=input()
    if 'push' in order:
        order,a=order.split()
        Q.push(a)
    elif 'pop' in order:
        print(Q.pop())
    elif 'front' in order:
        print(Q.front())
    elif 'back' in order:
        print(Q.back())
    elif 'size' in order:
        print(Q.size())
    elif 'empty' in order:
        print(Q.empty())
