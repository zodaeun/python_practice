print("사전 프로그램 시작... 종료를 q를 입력")
dic = {}
s = ''
#q를 입력하면 종료
while s != 'q':
    s = input("$ ")
    #검색 명령
    if s[0] == ">":
        if s[1:] in dic:
            print(dic[s[1:]])
        else:
            print("{}은/는 사전에 없습니다.".format(s[1:]))

    #입력 명령   
    elif s[0] == "<":
        #특수문자를 기준으로 단어 나눔.
        s = s[1:]
        inputStr = s.split(':')
        
        #단어와 뜻을 제대로 입력하지 않았을 때 오류 메시지
        if len(inputStr) < 2:
            print("입력오류발생")
        else:
            dic[inputStr[0]] = inputStr[1]
        
