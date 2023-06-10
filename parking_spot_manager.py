'''
무료주차장의 데이터를 분석하고 관리하기 위한 모듈
'''

class parking_spot:
    
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {
            'name': name,
            'city': city,
            'district': district,
            'ptype': ptype,
            'longitude': longitude,
            'latitude': latitude
        }


    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword='name'):
        return self.__item[keyword]

#문자열 리스트를 클래스 객체 리스트로 반환
def str_list_to_class_list(str_list):
    class_list = []
    for item in str_list:
        #쉼표를 기준으로 데이터 나누기
        values = item.split(',')
        name = values[1]
        city = values[2]
        district = values[3]
        ptype = values[4]
        longitude = float(values[5])
        latitude = float(values[6])
        spot = parking_spot(name, city, district, ptype, longitude, latitude)
        #클래스 리스트에 추가하기
        class_list.append(spot)
    return class_list    

#리스트에 저장된 모든 객체의 값 출력
def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(spot)


#VERSION 3) 필터링 기능 추가

# name으로 필터링
def filter_by_name(spots, name):
    return [spot for spot in spots if name in spot.get('name')]

# city로 필터링
def filter_by_city(spots, city):
    return [spot for spot in spots if city in spot.get('city')]

# district로 필터링
def filter_by_district(spots, district):
    return [spot for spot in spots if district in spot.get('district')]

# ptype 유형으로 필터링
def filter_by_ptype(spots, ptype):
    return [spot for spot in spots if ptype in spot.get('ptype')]

# locations로 필터링
def filter_by_location(spots, locations):
    min_lat, max_lat, min_long, max_long = locations
    return [spot for spot in spots if min_lat < spot.get('latitude') < max_lat and min_long < spot.get('longitude') < max_long]



#VERSION 4) 정렬 기능 추가

#주어진 키워드를 기준으로 parking_spot 객체의 리스트를 정렬하여 반환
def sort_by_keyword(spots, keyword):
    return sorted(spots, key = lambda spot: spot.get(keyword))



# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    #version2
    #import file_manager
    #str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    #spots = str_list_to_class_list(str_list)
    #print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)