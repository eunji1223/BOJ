while True:
    length=[]
    length=list(map(int,input().split()))
    if sum(length)==0:
        break
    else:
        maxlen=max(length)
        length.remove(maxlen)
        if ((length[0]**2) + (length[1]**2))==(maxlen**2):
            print("right")
        else:
            print("wrong")
    
    
