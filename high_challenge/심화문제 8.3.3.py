student_tup = (('211101', '최성훈', '010-1234-4500',4.3),('211102', '김은지', '010-2230-6540',3.9),('211103', '이세은', '010-3232-7788',4.25))

student_dic = {}


for i in range(len(student_tup)):
    student_dic[student_tup[i][0]]=[student_tup[i][1],student_tup[i][2],student_tup[i][3]]


print("학생의 정보 목록")
for i in student_dic.keys():
    print(i,':',student_dic[i])
