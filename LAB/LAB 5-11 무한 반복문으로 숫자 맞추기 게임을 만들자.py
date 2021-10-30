import random
n = 0
i = 0
answer = random.randint(1,10000)

 
while (n != answer and i < 10):
    n = int(input("숫자를 입력하세요: "))
    if n > answer:
        print(n," 보다 낮음")
    elif n < answer:
        print(n," 보다 높음")
    i = i + 1
        

if i >= 1:
    print("축하합니다.")
else:
    print("실패입니다.")
print("총 시도횟수 =",i)
