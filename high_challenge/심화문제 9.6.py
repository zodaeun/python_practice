import re

s = "English = 89, Science = 90, Math = 92, History = 80."

#정규화로 문자열에서 숫자로 된 문자 추출
score = re.findall('[0-9]+',s)
sList = []

for i in score:
    sList.append(float(i))

print("문장 s:", s)
print("총점:",sum(sList))
print("평균 점수:", sum(sList)/len(sList))
