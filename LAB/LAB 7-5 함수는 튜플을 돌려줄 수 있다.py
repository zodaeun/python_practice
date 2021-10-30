import math

def circle(r):
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return area, circum

radius = int(input("반지름을 입력하세요: "))
(x, y) = circle(radius)

print("원의 넓이는 {}이고 원의 둘레는 {}이다.".format(x, y))
    
