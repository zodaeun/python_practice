import random

n1 = random.randint(1,100)
n2 = random.randint(1,100)
 
print(n1,"+",n2,"=", end = " ")

answer = int(input())

if n1 + n2 == answer:
    print("잘했어요!!")
else:
    print("정답은", n1+n2,"입니다.")
