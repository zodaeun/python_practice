import turtle
t = turtle.Turtle()
t.shape("turtle")

while True:
    c = input("명령을 입력하세요(f/h/n): ")
    if c == "f":
        t.forward(100)
    elif c == "h":
        t.shapesize(10,10)
    elif c == "n":
        t.shapesize(3,3)
              
    
