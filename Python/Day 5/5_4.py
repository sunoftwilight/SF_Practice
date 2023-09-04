# ws_5_4.py

# 아래 함수를 수정하시오.
def capitalize_words(string):
    return string.title()

result = capitalize_words("hello, world!")
print(result)


def capitalize_words2(string):
    text = ' '.join(map(lambda x : x.capitalize(), string.split()))
    return text

result2 = capitalize_words2("hello, world!")
print(result2)


# review of professor
def capitalize_words3(text):
    words = text.split()
    capitalized_words = []
    for word in words :
        capitalized_words.append(word.capitalize())

    return ' '.join(capitalized_words)

result3 = capitalize_words3("hello, world!")
print(result3)