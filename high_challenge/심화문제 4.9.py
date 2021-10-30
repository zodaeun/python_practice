import turtle
t=turtle.Turtle()
t.shape("turtle")

x1, y1 = turtle.textinput("", "왼쪽 하단 모서리 좌표 x y").split()
x2, y2 = turtle.textinput("", "오른쪽 상단 모서리 좌표 x y").split()
x, y= turtle.textinput("", "점의 좌표").split()

t.goto(x1,y1)
t.goto(x2,y1)
t.goto(x2,y2)
t.goto(x1,y2)

if x >= x1 and x <= x2 and y >= y1 and y <= y2:
    print("점은 사각형 내부에 있습니다.")

print(x1,y1,x2,y2,x3,y3)
