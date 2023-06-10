'''
사용자와 상호작용하기 위한 UI(User Interface)를 제공하는 모듈

'''

# file_manager와 parking_spot_manager을 import하여 사용
import file_manager
import parking_spot_manager

def start_process(path):
    """
    프로그램의 실행 과정을 맡는 함수
    Args:
        path (string): 파일 경로
    """

    # file_manager 모듈의 read_file 함수를 호출하여 문자열 리스트를 반환
    str_list = file_manager.read_file(path)
    # parking_spot_manager 모듈의 str_list_to_class_list 함수로 parking_spot 객체의 리스트 반환
    spots = parking_spot_manager.str_list_to_class_list(str_list)

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        
        #parking_spot_manager 모듈의 print_spots 함수 호출
        if select == 1:
            parking_spot_manager.print_spots(spots)

        #이름, 시도, 시군구, 주차장유형, 위치를 기준으로 데이터를 분석하여 필터링   
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_long = float(input('type min long:'))
                max_long = float(input('type max long:'))
                locations = (min_lat, max_lat, min_long, max_long)
                spots = parking_spot_manager.filter_by_location(spots, locations)
            else:
                print("invalid input")
        #입력 받은 키워드에 대해 정렬
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            #입력받은 키워드에 대해 정렬하여 출력
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots, keyword)
            else: 
                print("invalid input")

        #Exit 출력하고 반복 종료
        elif select == 4:
            print("Exit") 
            break
        else:
            print("invalid input")