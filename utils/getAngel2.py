import math

def rotatecordiate(angle,rect):
    angle=angle*math.pi/180
    n=1600
    m=1200
    def onepoint(x,y):
        X = x * math.cos(angle) - y * math.sin(angle) -  n * math.cos(angle) + m * math.sin(angle) + n
        Y = y * math.cos(angle) + x * math.sin(angle) -  n * math.sin(angle) - m * math.cos(angle) + m
        return [int(X),int(Y)]
    newrect=[]
    for i in range(4):
        point=onepoint(rect[i*2],rect[i*2+1])
        newrect.extend(point)
    newrect.extend([1])
    print(newrect)
    return newrect