import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(-100,0)
t.write("x < y")
t.goto(0,0)
t.write("x = y")
t.goto(100,0)
t.write("x > y")
t.goto(0,100)
t.pendown

x = int(turtle.textinput("","x값을 입력하세요."))
y = int(turtle.textinput("","y값을 입력하세요."))

if x > y:
    t.goto(100,0)
elif x < y:
    t.goto(-100,0)
else:
    t.goto(0,0)
