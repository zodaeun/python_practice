items = {'커피음료':7, '펜':3, '종이컵':2, '우유':1, '콜라':4, '책':5}

menu = 0
while menu != 4:
    menu = int(input("메뉴를 선택하시오 1)재고조회 2)입고 3)출고 4)종료 "))
    
    if menu == 1:
        name = input("물건의 이름을 입력하시오: ")
        print("{}의 재고: {}".format(name, items[name]))
    if menu == 2:
        name, count = map(str, input("물건의 이름과 수량을 입력하시오: ").split())
        count = int(count)
        items[name] = items[name] + count
        print("{}의 재고: {}".format(name, items[name]))
    if menu == 3:
        name, count = map(str, input("물건의 이름과 수량을 입력하시오: ").split())
        count = int(count)
        items[name] = items[name] - count
        #재고가 0 이하면 출고를 취소함.
        if items[name] < 0:
            print("재고가 부족해 출고를 진행할 수 없습니다.")
            items[name] = items[name] + count
        
        print("{}의 재고: {}".format(name, items[name]))
        
print("프로그램을 종료합니다.")

    
