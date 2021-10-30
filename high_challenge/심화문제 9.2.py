n = input("문자열을 입력하세요: ")

lower = ''
upper = ''

for i in n:
    if i.islower() == True:
        lower = lower + i
    elif i.isupper() == True:
        upper = upper + i

print(lower+upper)
