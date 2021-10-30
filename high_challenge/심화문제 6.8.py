x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

def abs(x,y):
    if x - y > 0:
        return x-y
    else:
        return y - x

def distance(x1, y1, x2, y2):
    r = ((abs(x1,x2))**2 + (abs(y1,y2))**2)**0.5
    return r

print("두 점 사이의 거리는", distance(x1, y1, x2, y2))

