import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(10):
    x = random.randrange(2)
    if x == 0:
        t.right(90)
        t.forward(50)
    elif x == 1:
        t.left(90)
        t.forward(50)
    
