ID = "ilovepython"
PASSWORD = "mypass1234"

while True:
    id = input("아이디를 입력하세요: ")
    if id == ID:
        ps = input("비밀번호를 입력하세요: ")
        if ps == PASSWORD:
            print("환영합니다.")
            break
        else:
            print("비밀번호를 찾을 수 없습니다.")
    else:
        print("아이디를 찾을 수 없습니다.")
    

        
    
