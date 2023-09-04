# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(string):
    my_list = list(string)
    my_list.reverse()
    return ''.join(my_list)

result = reverse_string("Hello, World!")
print(result)


# solve with slicing
def reverse_string2(string):
    my_str = string[::-1]
    return my_str

result2 = reverse_string2("Hello, World!")
print(result2)


# review of professor
# str -> list -> str
def reverse_string3(text):
    lst = list(text)
    # print(reversed(lst))  # <list_reverseiterator object at 0x0000020C96BE9AF0>
    lst.reverse()           # None
    text = ''.join(lst)
    return text

result3 = reverse_string3("Hello, World!")
print(result3)


# 내장 함수 없이 변경하기 
# -> list의 인덱스를 밖에서부터 한 쌍씩 자리 변경 
# (안녕하세요 -> 안&요 자리 변경, 녕&세 자리 변경)
def reverse_string4(text):
    lst = list(text)
    for i in range(len(lst) // 2) :
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return ''.join(lst)

result4 = reverse_string4("Hello, World!")
print(result4)