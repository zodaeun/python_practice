dic = {}
word = ''

print("사전 프로그램 시작... 종료는 q를 입력")

while word != "q":
    word = input("$ ")

    if word[0] == '<':
        Word = word[1:]
        Word_str = Word.split(':')
        if len(Word_str) == 2:
            dic[Word_str[0]] = Word_str[1]
        else:
            print("잘못된 형식입니다.")

    elif word[0] == '>':
        Word = word[1:]
        if not Word in dic.keys():
            print("등록되지 않은 단어입니다.")
        else:
            print(dic[Word])

    elif word[0] == 'v':
        print("영어 사전에 있는 단어와 뜻을 출력합니다.")
        for i in dic.keys():
            print(i,':',dic[i])
            
        
