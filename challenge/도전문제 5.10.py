import random

n = random.randint(1,100)
x = 0
t = 0

while x != n and t < 10:
    if x > n:
        print("x가 n보다 큽니다.")
        x = int(input("숫자를 입력하세요: "))
    else:
        print("x가 n보다 작습니다.")
        x = int(input("숫자를 입력하세요: "))
    t = t + 1
    
if t == 10:
    print("실패입니다.")
else:
    print("성공입니다.")
