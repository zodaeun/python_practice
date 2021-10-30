city_info =[('서울',9765),('부산',3441),('인천',2954),('광주', 1501),('대전',1531)]

max_pop = 0
min_pop = 9999
total_pop = 0

max_city = None
min_city = None

for city in city_info: # city = (도시, 인구)
    total_pop = total_pop + city[1] 
    if city[1] > max_pop:
        max_pop = city[1]
        max_city = city
    elif city[1] < min_pop:
        min_pop = city[1]
        min_city = city
    

print("최대 인구: {}, 인구: {}천명".format(max_city[0], max_city[1]))
print("최소 인구: {}, 인구: {}천명".format(min_city[0], min_city[1]))
print("리스트 도시 평균 인구: {}천명".format(total_pop / len(city_info)))
