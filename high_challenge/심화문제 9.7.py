import string

t = input("문장을 입력하시오: ")
n = int(input("이동시킬 칸 수를 입력하시오: "))
tList = list(t)

src = string.ascii_uppercase+string.ascii_lowercase
dst = src[n:]+src[:n]

output = ''
for i in tList:
    if i in src:
        output = output + dst[src.index(i)]
    else:
        output = output + i

print(output)
    
