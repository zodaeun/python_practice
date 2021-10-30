fruit = []

for i in range(3):
    x = input("좋아하는 과일 이름을 입력하시오. ")
    fruit.append(x)

favorite = input("과일의 이름을 입력하시오. ")

if favorite in fruit:
    print("이 과일은 당신이 좋아하는 과일입니다.")
else:
    print("이 과일은 당신이 좋아하는 과일이 아닙니다.")
