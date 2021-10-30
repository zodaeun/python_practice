n = int(input("세 자리 정수를 입력하시오: "))

h = n // 100
t = (n % 100) // 10
o = n % 10

print("백의자리: ", h)
print("십의자리: ", t)
print("일의자리: ", o)
