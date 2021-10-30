import random
import turtle

t = turtle.Turtle()
t.shape("turtle")


for i in range(30):
    l = random.randint(1,100)
    t.forward(l)
    a = random.randint(0,360)
    t.left(a)
