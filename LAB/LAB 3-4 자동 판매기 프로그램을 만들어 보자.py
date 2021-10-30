money = int(input("투입한 돈: "))
price = int(input("물건 값: "))

change = money - price
coin5 = change // 500
coin1 = change % 500 // 100

print("거스름돈: ",change)
print("500원 동전의 개수: ", coin5)
print("100원 동전의 개수: ", coin1)

