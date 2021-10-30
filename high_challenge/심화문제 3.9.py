s = float(input("평균 시속(km/h)을 입력하세요: "))
h = float(input("이동시간(h)을 입력하세요: "))

print("평균 시속:",s)
print("이동 시간:",h)

print("이동 시간:", int(h // 1),"시간", int(h % 1 *60),"분",int((h % 1 *60) % 1 * 60),"초")
print("이동 거리:", s * h,"km")
