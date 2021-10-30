def weeklyPay(rate, hour):

    if hour > 30:
        money = (rate * 30) + rate * 1.5 * (hour-30)
    else:
        money = rate * hour
    
    return money

rate = int(input("시급을 입력하시오: "))
hour = int(input("근무 시간을 입력하시오: "))

x = weeklyPay(rate, hour)

print("주급은 ",x)
