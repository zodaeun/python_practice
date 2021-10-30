import string

upper_src_str = string.ascii_uppercase
upper_dst_str = upper_src_str[3:]+upper_src_str[:3]
lower_src_str = string.ascii_lowercase
lower_dst_str = lower_src_str[3:]+lower_src_str[:3]

def upper_kaisar(a):
    idx = upper_src_str.index(a)
    return upper_dst_str[idx]

def lower_kaisar(a):
    idx = lower_src_str.index(a)
    return lower_dst_str[idx]



s= input("문장을 입력하시오: ")
print("암호화 된 문자: ", end = "")

for i in s:
    if i in upper_src_str:
        print(upper_kaisar(i), end = "")
    elif i in lower_src_str:
        print(lower_kaisar(i), end = "")
    else: #공백 입력
        print(i, end = "")

print()
