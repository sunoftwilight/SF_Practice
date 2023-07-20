import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'


black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']


def create_user(list):

    for item in list:

        censored_user_list = {
            list['company'] : list['name']
        }

    return censored_user_list


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

    dummy_data.append(user_info)





a = create_user(user_info)

print(a)

# users = []
# users.append(create_user)

# def censorship():
    
#     for i in range(1,11):
#         if users[i].keys() in black_list:
#             print(f'{users}')
    

#     if  in