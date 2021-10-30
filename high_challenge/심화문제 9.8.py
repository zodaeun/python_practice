import re

t = 'Jian777 and 777Jian is very famous Data scientist. He is only 26 years old but publiched 19 papers.'
print(t)

tList = t.split()
eng = ''
num = ''
eng_num = ''

print()
print("영문 단어: ", end = "")
for i in tList:
    if i.isalpha() == True:
        print(i, end = " ")

print()
print("숫자: ", end = "")
for i in tList:
    if i.isdigit() == True:
        print(i, end = " ")

print()
print("영문자+숫자: ", end = "")
print(re.findall('[0-9]+[a-zA-Z]+|[a-zA-Z]+[0-9]+',t))
