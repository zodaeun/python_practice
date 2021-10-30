import re
txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'

email = re.findall('[a-z]+@[a-z]+\.com',txt)
print('추출된 이메일: ',email)


print("추출된 아이디: ",re.findall('^[a-z]+',email[0]), ", 도메인: ",re.findall('[a-z]+\.com',email[0]))
print("추출된 아이디: ",re.findall('^[a-z]+',email[1]), ", 도메인: ",re.findall('[a-z]+\.com',email[1]))


