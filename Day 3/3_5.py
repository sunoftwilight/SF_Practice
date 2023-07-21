# 실습 번호.py
import book

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
  
    user_info = {'name': name, 'age' : age, 'address' : address}
    print(f'{name}님 환영합니다!')
    
    return user_info


many_user = list(map(create_user, name, age, address))


info = dict(map(lambda human : {'name':human['name'], 'age':human['age']}, many_user))


def rental_book(info):
    name = info['name']
    count = info['age'] // 10
    book.decrease_book(count)
    print(f'{name}님이 {count}권의 책을 대여하였습니다.')
    
rental_book(info)
