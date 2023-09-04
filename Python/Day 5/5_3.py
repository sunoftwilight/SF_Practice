# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(num_tpl):
    new_tuple = list(num_tpl)       # list로 변경하지 않고 sorted() 사용하면 됨!
    new_tuple.sort()
    return tuple(new_tuple)

result = sort_tuple((5, 2, 8, 1, 3))
print(result)


# review of professor
# sorted()
def sort_tuple2(t):
    new_tuple = ()
    new_tuple = tuple(sorted(t))
    return new_tuple

result2 = sort_tuple2((5, 2, 8, 1, 3))
print(result2)


# for문
def sort_tuple3(t):
    new_tuple = ()
    sorted_list = sorted(t)
    for item in sorted_list :
        new_tuple += (item, )      # new_tuple = (1,) + (2,)  ->  (1, 2)
    return new_tuple

result3 = sort_tuple3((5, 2, 8, 1, 3))
print(result3)