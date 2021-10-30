n = int(input("정수를 입력하세요: "))

print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", end = " ")

if n % 2 == 0:
    if n >=0 and n <= 100:
        print("True")
    else:
        print("False")
else:
    print("False")
        
    
