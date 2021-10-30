#문자열 이용하는 방법
name = input("이름을 입력하시오: ")

sName = name.split()

print(sName[1])

#입력을 세 단어로 받는 방법
fst,mid, lst = map(str, input("이름을 입력하시오: ").split())

print("중간이름은: ",mid)
