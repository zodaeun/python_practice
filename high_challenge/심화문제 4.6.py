print("우리 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")

food = ["햄버거(입력 b)","치킨(입력 c)","피자(입력p)"]

choice = input("메뉴를 선택하세요(알파벳 b,c,p 입력) : ")

if choice == "b":
    print("햄버거를 선택하였습니다.")
elif choice == "c":
    print("치킨을 선택하였습니다.")
elif choice == "p":
    print("피자를 선택하였습니다.")
else:
    print("선택한 메뉴가 없습니다.")
