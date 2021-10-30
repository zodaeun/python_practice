import random

n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
n = [n1,n2,n3]

x,y,z = map(int,input("세 복권번호를 입력하시오: ").split())

print("복권번호:",n1,n2,n3)

if (x in n) and (y in n) and (z in n):
    print("상금 1억원")
elif (x in n and y in n) or (x in n and z in n) or (y in n and z in n):
    print("상금 1천만원")
elif (x in n) or (y in n) or (z in n):
    print("상금 1만원")
else:
    print("다음 기회에..")


