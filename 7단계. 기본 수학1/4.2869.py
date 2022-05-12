import math
A,B,V=map(int,input().split())
#A*k-B(k-1)=>V 이항 k=>(V-B)/(A-B)
k = (V-B)/(A-B)
print(math.ceil(k))
    
    
    
