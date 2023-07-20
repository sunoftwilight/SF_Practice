# ws_3_3.py
import book

def rental_book(name, count):
    book.decrease_book(count)
    print(f'{name}님이 {count}권의 책을 대여하였습니다.')

rental_book('홍길동', 3)
