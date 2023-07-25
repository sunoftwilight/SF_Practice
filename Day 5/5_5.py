# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(num_list):
    even = []

    for _ in range(len(num_list)):
        if num_list[-1] % 2 == 0 :
            even.append(num_list.pop(-1))

        num_list.pop(-1)
        
    num_list.extend(even)
    
    return num_list[::-1]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[-1])
result = even_elements(my_list)
print(result)



# review of professor
# 단순 코드 - pop, extend 사용X
def even_elements2(lst):
    result = []
    for num in lst:
        if num % 2 ==0:
            result.append(num)
    return result


my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result2 = even_elements2(my_list2)
print(result2)



# pop, extend 사용 O
def even_elements3(lst):
    result = []
    # for문 사용시 pop에 의해 list의 길이 계속 달라지므로 인덱스 접근 시range out 발생 -> while문 사용            
    while lst:                        # lst안에 요소가 남아 있는 동안 실행
        item = lst.pop(0)             # lst의 가장 앞 요소부터 pop하여 item에 할당
        if item % 2 == 0 :            # item이 짝수이면 result list에 추가
            result.extend([item])
    return result


my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result3 = even_elements3(my_list3)
print(result3)



# for문 사용
def even_elements4(lst):
    result = []
    l = len(lst)
    for i in range(l):                        
        item = lst.pop(0)             
        if item % 2 == 0 :            
            result.extend([item])
    result.reverse()
    return result


my_list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result4 = even_elements3(my_list4)
print(result4)