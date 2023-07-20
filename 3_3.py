# ws_3_3.py
# 파이썬에서 파일 하나하나는 =Module

import book
# from book import decrease_book ... (a)

def rental_book(name, count):
    book.decrease_book(count)   
    # (a) 형식으로 import할 경우 decrease_book(count)로 작성
    print(f'{name}님이 {count}권의 책을 대여하였습니다.')


rental_book('홍길동', 3)