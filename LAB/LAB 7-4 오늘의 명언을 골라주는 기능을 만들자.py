import random

q = []
q.append("꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.")
q.append("분노는 바보들의 가슴속에서만 살아간다.")
q.append("고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")
q.append("사람은 사랑할 때 누구나 시인이 된다.")
q.append("시작이 반이다.")

print("#"*15)
print("#", "오늘의 명언", "#")
print("#"*15)
print()
print(random.choice(q))
