import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

for i in range(1, 11):
    API_URL_10 = (API_URL + str(i))
    response = requests.get(API_URL_10)  # API 요청
    parsed_data = response.json()        # JSON -> dict 데이터 변환

    

    if float(user_info['lat']) < 80:
        if float(user_info['lng']) > -80:
            user_info = {
                'name' : parsed_data['name'], 
                'lat' : parsed_data['address']['geo']['lat'],
                'lng' : parsed_data['address']['geo']['lng'],
                'company' : parsed_data['company']['name']
            }
            dummy_data.append(user_info)

print(dummy_data)