import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def n_polygon(n, length):

    for i in range(n):
        t.forward(length)
        t.left(360/n)
    return 0

for i in range(18):
    t.left(20)
    n_polygon(6,50)

