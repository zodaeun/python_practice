import turtle
t = turtle.Turtle()
t.shape("turtle")

t.color("blue")
t.fillcolor("red")
t.pensize(3)
t.speed(0)

t.right(90)

mylist = [120,56,309,156,23,98]

for i in range(len(mylist)):
    t.begin_fill()
    t.left(180)
    t.forward(mylist[i])
    t.right(90)
    t.write(mylist[i])
    t.forward(15)
    t.right(90)
    t.forward(mylist[i])
    t.end_fill()
