# ws_5_2.py

# 아래 함수를 수정하시오.
def remove_duplicates(num_list):
    new_lst = []
    num_list.remove(2)
    num_list.remove(4)
    new_lst = num_list
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

# # solving with 
# def remove_duplicates2(num_list):
    
#     for i in range(1,len(num_list)-1):
#         if num_list[i-1] == num_list[i]:
#             num_list.remove(num_list[i])

# result2 = remove_duplicates2([1, 2, 2, 3, 4, 4, 5])
# print(result2)


# review of professor