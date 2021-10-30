def max_and_min(n1,n2,n3):
    r1 = max(n1,n2,n3)
    r2 = min(n1,n2,n3)
    return r1,r2

a,b,c = map(int,input("세 수를 입력하세요: ").split())

print("가장 큰 수:",max_and_min(a,b,c)[0])
print("가장 작은 수:",max_and_min(a,b,c)[1])
