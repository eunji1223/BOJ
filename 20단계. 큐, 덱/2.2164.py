import sys
input=sys.stdin.readline

class Queue:
    def __init__(self):
        self.items=[]
        self.first_index=0
    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        x=self.items[self.first_index]
        self.first_index+=1
        return x
    def front(self):
        return self.items[self.first_index]
    def size(self):
        num=len(self.items)-self.first_index
        if num<1:
            return -1
        else:
            return num

N=int(input())
Q=Queue()
for i in range(1,N):
    Q.enqueue(i)
while(Q.size()!=-1):
    Q.dequeue()
    num = Q.dequeue()
    Q.enqueue(num)
print(Q.front())
