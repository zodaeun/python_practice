student_tup = (('211101', '최성훈', '010-1234-4500'),('211102', '김은지', '010-2230-6540'),('211103', '이세은', '010-3232-7788'))

student_dic = {}


for i in range(len(student_tup)):
    student_dic[student_tup[i][0]] = [student_tup[i][1], student_tup[i][2]]

studentNum = input("학번을 입력하시오: ")

studentName = student_dic[studentNum][0]
studentPhoneNum = student_dic[studentNum][1]

print("이름:", studentName)
print("연락처:", studentPhoneNum)

    
