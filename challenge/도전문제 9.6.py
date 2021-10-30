import re

txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'

email = re.findall('[a-z]+@[a-z]+.[a-z]+',txt)

print(re.findall('^[a-z]+',email[0]),re.findall('[a-z]+\.[a-z+]+',email[0]))
print(re.findall('^[a-z]+',email[1]),re.findall('[a-z]+\.[a-z+]+',email[1]))
