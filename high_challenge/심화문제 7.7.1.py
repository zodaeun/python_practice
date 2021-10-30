fruit_list = ["banana","orange","kiwi","apple","melon"]
del_fruit_list = []

long = fruit_list[0]

print("길이가 가장 긴 문자열:",end = " ")
for i in range(len(fruit_list)):
    if len(fruit_list[i]) >= len(long):
        long = fruit_list[i]
        del_fruit_list.append(long)

print(del_fruit_list)
fruit_list = fruit_list + del_fruit_list
print(fruit_list)
