deep = -30
day = 0

while deep < 0:
    deep = deep + 7
    day = day + 1
    print("day : {0} 달팽이의 위치 : {1} 미터".format(day, deep))
    if deep < 0:
        deep = deep - 5


print("축하합니다. 우물을 탈출했습니다.")
print("우물을 탈출하는 데 걸린 날은",day,"일 입니다.")
