import random

options = ["좌측","중앙","우측"]
computer = random.choice(options)

x = input("어디를 공격하시겠어요? (좌측/중앙/우측): ")

print("컴퓨터의 수비위치:",computer)
if x == computer:
        print("공격에 실패했습니다.")
else:
    print("공격에 성공했습니다.")
