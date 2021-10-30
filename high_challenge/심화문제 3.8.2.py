n = int(input("세 자리 정수를 입력하시오: "))

n1 = n % 10 
n10 = (n % 100) // 10
n100 = n // 100

print(n1, end = "")
print(n10, end = "")
print(n100, end = "")

