# ws_5_4.py

# 아래 함수를 수정하시오.
def capitalize_words(string):
    return string.title()


def capitalize_words2(string):
    text = ' '.join(map(lambda x : x.capitalize(), string.split()))
    return text


result = capitalize_words("hello, world!")
print(result)

result2 = capitalize_words2("hello, world!")
print(result2)