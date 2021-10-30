import turtle
t = turtle.Turtle()
t.shape("turtle")



def f(x):
    y = x**2 + 1
    return y

t.goto(200,0)
t.goto(0,0)
t.goto(0,200)
t.goto(0,0)

for x in range(150):
    t.goto(x, int(0.01*f(x)))
