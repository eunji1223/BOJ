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
        print("실행")
        if self.size()==0 or self.front==len(self.items):
            print("실행")
            return -1
        else:
            print(self.items[self.front])
            return self.items[self.front]
    def back(self):
        if self.size()==0 or self.front==len(self.items):
            return -1
        else:
            return self.items[-1]
    def empty(self):
        if self.size()==0:
            return 1
        else: return 0
        
Q=Queue()
N=int(input())
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


        
