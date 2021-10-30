student_tup = (('211101', '최성훈', '010-1234-4500',4.3),('211102', '김은지', '010-2230-6540',3.9),('211103', '이세은', '010-3232-7788',4.25))

student_dic = {}
s = 0

#튜플 값 딕셔너리에 넣음
for i in range(len(student_tup)):
    student_dic[student_tup[i][0]]=[student_tup[i][1],student_tup[i][2],student_tup[i][3]]

#딕셔너리의 3번째 값(성적)들의 합
for i in student_dic.values():
    s = s + i[2]

print("전체 학생의 학점 평균 : {}".format(s/3))

