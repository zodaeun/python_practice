a,b,c = map(int, input("세 정수를 입력하시오: ").split())

if a>b:
    if a>c:
        if b>c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if b>c:
        if a>c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        print(c,b,a)
