def create_user(name, age, address):

    user_info = {
        'name': name, 
        'age' : age, 
        'address' : address
    }

    print(f'{name}님 환영합니다!')
    
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


users = list(map(create_user, name, age, address))
# map에서 적용할 함수 create_user
# map이 함수를 적용할 iterable - name, age, address
#                               => 각각에 적용하여 하나의 원소화
# 반환된 유저 정보를 하나의 리스트 users에 담기 위해 list화

print(users)