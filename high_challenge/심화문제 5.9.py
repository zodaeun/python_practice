nlist = []
n = 0

while True:
    n = int(input("정수를 입력하시오: "))
    if n == -99:
        break
    nlist.append(n)

print(len(nlist),"개의 유효한 정수 중 가장 큰 정수는",max(nlist),"이고","가장 작은 정수는",min(nlist),"입니다.")
