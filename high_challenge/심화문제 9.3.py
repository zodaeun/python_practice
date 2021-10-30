n = input("문자열을 입력하세요: ")

upper = 0
lower = 0
num = 0
special = 0

for i in n:
    if i.isupper() == True:
        upper = upper + 1
    elif i.islower() == True:
        lower = lower + 1
    
    elif i.isdigit() == True:
        num = num + 1
    else:
        special = special + 1

print(upper)
print(lower)
print(num)
print(special)
