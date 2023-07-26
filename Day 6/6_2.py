# ws_6_2.py

# 아래 함수를 수정하시오.
def get_value_from_dict(dictionary, key):
    return dictionary.get(key)

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice



# Review of professor
def get_value_from_dict2(dictionary, key):
    return dictionary[key]

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict2(my_dict, 'name')
print(result) # Alice