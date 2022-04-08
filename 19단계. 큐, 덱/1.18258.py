class Queue:
    def __init__(self):
        self.items=[]
        self.front=0
    def __len__(self):
        return len(self.items)-self.front
    def size(self):
        return len(self.items)-self.front
    def push(self,val):
        self.items.append(val)
    def pop(self):
        if len(self.items)==0 or self.front==len(self.items):
            return -1
        else:
            x=self.items[self.front]
            self.front+=1
            return x
    def front(self):
        if len(self.items)==0 or self.front==len(self.items):
            return -1
        else:
            return self.items[self.front]
    def back(self):
        if len(self.items)==0 or self.front==len(self.items):
            return -1
        else:
            return self.items[-1]
    def empty(self):
        if self.size(self)==0:
            return 1
        else: return 0
        
Q=Queue()
N=int(input())
for i in range(N):
    order=input()
    if order in 'push':
        order,a=order.split()
        print(Q.push())
    elif order in 'pop':
        print(Q.pop())
    elif order in 'front':
        print(Q.front())
    elif order in 'back':
        print(Q.back())
    elif order in 'size':
        print(Q.size())
    elif order in 'empty':
        print(Q.empty())

        
