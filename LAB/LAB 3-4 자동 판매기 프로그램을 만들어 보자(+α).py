money = int(input("투입한 돈: "))
price = int(input("물건값: "))

change = money - price
print("거스름돈: ", change)

cash = change // 1000
coin500 = change % 1000 // 500
coin100 = change % 500 // 100
coin50 =  change % 100 // 50
coin10 = change % 100 % 50 // 10

print("1000원: {0}개".format(cash))
print("500원: {0}개".format(coin500))
print("100원: {0}개".format(coin100))
print("50원: {0}개".format(coin50))
print("10원: {0}개".format(coin10))

