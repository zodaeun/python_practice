print("1)덧셈 2)뺄셈 3)곱셈 4)나눗셈")
op = int(input("어떤 연산을 원하는지 번호를 입력하세요: "))

print("연산을 원하는 숫자 두 개를 입력하세요: ")
n1 = int(input())
n2 = int(input())

if op == 1:
    print(n1,"+",n2,"=",n1+n2)
elif op == 2:
    print(n1,"-",n2,"=",n1-n2)
elif op == 3:
    print(n1,"x",n2,"=",n1*n2)
elif op == 4:
    print(n1,"%",n2,"=",n1/n2)
else:
    print("잘못된 번호입니다.")

