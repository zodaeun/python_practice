import turtle
t = turtle.Turtle()
t.shape("turtle")


t.penup()
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다.")

t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")

t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(0,0)
t.pendown


n = int(turtle.textinput("","숫자를 입력하세요."))

if n > 0 :
    t.goto(100,100)
elif n == 0:
    t.goto(100,0)
else:
    t.goto(100,-100)
