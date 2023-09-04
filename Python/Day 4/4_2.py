import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'


dummy_data = []

for i in range(1, 11):
    API_URL_10 = (API_URL + str(i))
    response = requests.get(API_URL_10)  # API 요청
    parsed_data = response.json()        # JSON -> dict 데이터 변환
    name = parsed_data['name']
    dummy_data.append(name)


print(dummy_data)


# Review of Professor
dummy_data = []

for i in range(1, 11):
    API_URL_10 = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL_10).json()  # API 요청
    dummy_data.append(response.get('name'))

print(dummy_data)