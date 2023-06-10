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