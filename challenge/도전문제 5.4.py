import turtle
t = turtle.Turtle()
t.shape("turtle")

num = int(turtle.textinput("", "몇각형을 그릴까요? 숫자를 입력해주세요."))

for i in range(1, num+1):
    t.forward(50)
    t.left(360/num)
    
