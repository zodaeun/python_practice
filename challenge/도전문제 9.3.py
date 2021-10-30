import random
import string

n = int(input("몇 자리의 비밀번호를 원하십니까? "))

src = string.ascii_uppercase + string.ascii_lowercase + '0123456789'


pw = ''
for i in range(n):
    pw = pw + src[random.randrange(0,len(src))]

print(pw)
