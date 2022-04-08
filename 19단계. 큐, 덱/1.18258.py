queue=[]
N=int(input())
for i in range(N):
    order=input()
    if order in 'push':
        order,a=order.split()
        queue.append(a)
    elif order=='pop':

    elif order=='size':
        print(len(queue))
    elif order=='empty':
        if len(queue)==0:
            print('1')
        else:
            print('0')
    elif order=='front':
        print(queue[0])
    elif order=='back':
        print(queue[-1])
