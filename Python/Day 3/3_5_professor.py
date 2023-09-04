from book import decrease_book

def create_user(name, age, address):

    user_info = {
        'name': name, 
        'age' : age, 
        'address' : address
    }

    print(f'{name}님 환영합니다!')
    
    return user_info


def rental_book(info):     # info : 신규 고객의 이름과 나이를 담은 dict
    decrease_book(info['age'])
    print(f"{info['name']}님이 {info['age']}권의 책을 대여하였습니다.")


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


many_users = list(map(create_user, name, age, address))
# 실행 결과 : [{'name': '김시습', 'age': 20, 'address': '서울'}, {'name': '허균', 'age': 16, 'address': '강 
# 릉'}, {'name': '남영로', 'age': 52, 'address': '조선'}, {'name': '임제', 'age': 36, 'address': '나주'}, {'name': '박지원', 'age': 60, 'address': '한성부'}]

# map에서 적용할 함수 create_user
# map이 함수를 적용할 iterable - name, age, address
#                               => 각각에 적용하여 하나의 원소화
# 반환된 유저 정보를 하나의 리스트 many_users에 담기 위해 list화


map(lambda x: {'name': x['name'], 'age' : x['age'] // 10}, many_users)
# map과 lambda를 이용하여 info dict 생성
# many_users라는 시퀀스의 요소 각각에 lambda 함수 적용
# many_users의 key 중 name의 값을 info의 name의 값으로 넣어라
# many_users의 key 중 age가 가지는 값을 //10 연산하여 info의 age 값으로 할당

""" lambda 함수 해석
def f(x):
    user = {
        'name' : x['name'],
        'age' : x['age'] // 10
    }
    return user
"""


list(map(rental_book, map(lambda x: {'name': x['name'], 'age' : x['age'] // 10}, many_users)))
# map(~~)의 결과는 시퀀스 - 해당 시퀀스 각 요소에 대해 rental_book 함수 적용


"""map 대신 zip을 이용한 방식

user_info = []

for n, a, ad in zip(name, age, address):
    user_info.append({
        'name' : n,
        'age' : a,
        'address' : ad
    })
    print(f'{n}님 환영합니다.')

for info in user_info:
    rental_book({
        'name' : info['name'],
        'age' : info['age'] // 10
    })

"""