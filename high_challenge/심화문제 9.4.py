a = 'ABCD'
b = '1234'

print("a = {}".format(a))
print("b = {}".format(b))

str1 = ''
str2 = ''

for i in range(len(a)):
    str1 = str1 + a[i]+b[i]
    str2 = str2 + a[len(a)-1-i] + b[len(b)-1-i] 

print(str1)
print(str2)

