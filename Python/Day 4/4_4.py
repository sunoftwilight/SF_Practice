# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'


black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']


def create_user(user_list):        # dummy_data가 인자

    censored_user_list = {}        # company name = key, name = value

    for data in user_list:
        if censorship(data) :
            censored_user_list[data['company']] = data['name'].split("=")

    return censored_user_list


def censorship(TF_user):              
    
    if TF_user['company'] in black_list:
        print(f"{TF_user['company']} 소속의 {TF_user['name']}은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상없습니다')
        return True


dummy_data = []

for i in range(1,11):   
    API_URL_10 = (API_URL + str(i))    
    response = requests.get(API_URL_10)  # API 요청    
    parsed_data = response.json()        # JSON -> dict 데이터 변환

    user_info = {
        'name' : parsed_data['name'], 
        'lat' : parsed_data['address']['geo']['lat'],
        'lng' : parsed_data['address']['geo']['lng'],
        'company' : parsed_data['company']['name']
    }

    if float(user_info['lat']) < 80:
        if float(user_info['lng']) > -80:
            dummy_data.append(user_info)




print(create_user(dummy_data))