nlist = input("문자열을 입력하세요: ")

for i in range(len(nlist)):
    print(nlist[:i])

for i in range(len(nlist)):
    print(nlist[:len(nlist)-i])
