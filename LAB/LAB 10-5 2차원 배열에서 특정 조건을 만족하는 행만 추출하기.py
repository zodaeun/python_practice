import numpy as np

players = [[170,76.4],
           [183,86.2],
           [181,78.5],
           [176,80.1]]

np_player = np.array(players)

r1 = np_player[np_player[:,1] >= 80]
r2 = np_player[np_player[:,0] >=180]

print("몸무게가 80kg 이상인 선수 정보")
print(r1)
print("키가 180cm 이상인 선수 정보")
print(r2)
