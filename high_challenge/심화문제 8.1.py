fruits_price= {'사과':0,'배':0,'수박':0,'귤':0,'포도':0}

a,b,c,d,e = map(int, input("사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력: ").split())

fruits_price['사과'] = a
fruits_price['배'] = b
fruits_price['수박'] = c
fruits_price['귤'] = d
fruits_price['포도'] = e

print("-"*10,"오늘의 과일 가격","-"*10)
for i in fruits_price.keys():
    print("{}:{}원".format(i,fruits_price[i]))
