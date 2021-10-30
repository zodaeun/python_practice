s = 0

a = int(input("시작 정수를 입력하세요 : "))
b = int(input("끝 정수를 입력하세요 : "))


for i in range(a, b+1):
    s = s + i

print(a,"에서",b,"까지 정수의 합:",s)
