fruits_price= {'사과':0,'배':0,'수박':0,'귤':0,'포도':0}

a,b,c,d,e = map(int, input("사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력: ").split())

fruits_price['사과'] = a
fruits_price['배'] = b
fruits_price['수박'] = c
fruits_price['귤'] = d
fruits_price['포도'] = e

fruit = input("구매를 원하는 과일의 이름을 입력하시오: ")

print("오늘의 {} 가격은 {}원 입니다.".format(fruit,fruits_price[fruit]))
