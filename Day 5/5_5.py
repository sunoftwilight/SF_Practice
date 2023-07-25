# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(num_list):
    even = []

    for i in range(len(num_list)):
        if num_list[-1] % 2 == 0 :
            even.append(num_list.pop(-1))

        num_list.pop(-1)
        
    num_list.extend(even)
    
    return num_list[::-1]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
