print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
menu = ["햄버거","치킨","피자"]

print("1)",menu[0])
print("2)",menu[1])
print("3)",menu[2])

x = int(input("1에서 3까지의 메뉴를 선택하세요: "))


while x not in [1,2,3]:
    x = int(input("메뉴를 다시 입력하세요: "))
    

print(menu[x-1],"을 선택하였습니다.")
