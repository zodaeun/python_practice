import re

s = "Korea i awesome! I REALLY LOVE KOREA."

c = re.findall('KOREA|Korea|korea', s)
print("Korea의 출현 횟수: ",len(c))


