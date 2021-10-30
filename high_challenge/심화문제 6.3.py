def max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
def min(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1  and n2 < n3:
        return n2
    else:
        return n3

n1,n2,n3 = map(int,input("숫자 세 개를 입력하세요: ").split())

print("가장 큰 수는", max(n1,n2,n3))
print("가장 작은 수는", min(n1,n2,n3))

