list1 = [3,5,7]
list2 = [2,3,4,5,6]

for i in range(len(list1)):
    for j in range(len(list2)):
        print(list1[i],"x",list2[j], "=", list1[i]*list2[j])
