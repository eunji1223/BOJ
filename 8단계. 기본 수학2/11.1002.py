import math
test = int(input())

for _ in range(test):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    #distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    if x1 == x2 and y1 == y2: # 두 점이 서로 동일할 때
        if r1 == r2: #반지름도 같을 때(위치의 개수 무한)
            print(-1)
        else: # 두 원이 겹치지 않을 때(위치의 개수 없음)
            print(0)
    
    else:
        if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2:
            # 한 쪽의 반지름이 두 점 사이의 거리와 반지름을 더한 값보다 큰 경우 = 만나는 점이 없음
            print(0)
        elif r1 == distance + r2 or r2 == distance + r1 or r1 + r2 == distance:
            # 한 점에서만 만날 경우
            print(1)
        else:
            # 두 점이 만날 경우
            print(2)
