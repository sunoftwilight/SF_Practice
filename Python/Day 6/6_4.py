# ws_6_4.py

# 아래 함수를 수정하시오.
def get_keys_from_dict(dictionary):
    return list(dictionary.keys())

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)



# Review of professor
def get_keys_from_dict2(dictionary):
    keys =[]
    for key in dictionary :
        keys.append(key)
    return keys

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict2(my_dict)
print(result)