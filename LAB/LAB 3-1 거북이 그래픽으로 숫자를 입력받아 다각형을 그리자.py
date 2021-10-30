import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

n = int(turtle.textinput("","몇각형을 그리시겠어요?"))

for i in range(n):
    t.forward(50)
    t.left(360/n)

turtle.done()
