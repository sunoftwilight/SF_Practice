number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    

def create_user(name, age, address):   # 함수가 name, age, address를 인자로 받음
    
    increase_user()
    
    user_info = {
        'name': name, 
        'age' : age, 
        'address' : address
    }                                    # 딕셔너리 형태

    # user_info = {}
    # user_info['name'] = name
    # user_info['age'] = age
    # user_info['adress'] = adress       # 위와 동일한 기능

    print(f'{name}님 환영합니다!')
    
    return user_info        # user_info 딕셔너리 반환


print(f'현재 가입 된 유저 수 : {number_of_people}')
print(create_user('홍길동', 30, '서울'))
print(f'현재 가입 된 유저 수 : {number_of_people}')