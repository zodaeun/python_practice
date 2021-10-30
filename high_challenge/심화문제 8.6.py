student_tuple = [('211101','강이안','010-123-1111'),('211102','박동민','010-123-2222'),('211103','김수정','010-123-3333')]

student_dic = {}

for num, name, phone in student_tuple:
    student_dic[num] = [name,phone]

for i in student_dic.keys():
    print(i,':',student_dic[i][0])

num = input("학번을 입력하세요: ")

print('{} 학생은 {}이며, 전화번호는 {}입니다.'.format(num, student_dic[num][0],student_dic[num][1]))
