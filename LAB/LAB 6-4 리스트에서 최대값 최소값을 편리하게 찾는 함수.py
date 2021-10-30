
def getMinMax(list_data, method):
    if method == "Max":
        list_Max = list_data[0]
        
        for i in range(5):
            if list_Max < list_data[i]:
                list_Max = list_data[i]

        print(list_Max)
    elif method == "Min":
        list_Min = list_data[0]

        for i in range(5):
            if list_Min > list_data[i]:
                listMin = list_data[i]
        print(list_Min)
    else:
        print("정확히 입력하세요")

list_data = [27, 90, 30, 87, 56]

print(list_data)

while True:
    s = input("Max/Min? ")
    getMinMax(list_data, s)
