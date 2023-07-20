information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

'''
- 작가와 작품 목록 참고
- 허균 : 홍길동전, 장생전, 도문대작
- 임제 : 수성지, 백호집, 원생몽유록
- 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
'''
information = {
    authors[0] : books[1], 
    authors[1] : books[3], 
    authors[2] : books[4], 
    authors[3] : books[0], 
    authors[4] : books[2]
}

# 내가 짠 코드 (.keys 사용)
# authors_list = list(information.keys())

# for i in range(5):
#     print(f'{authors_list[i]} : {information[authors[i]]}')


# 교수님이 짠 코드 (.items 사용 - key & value 동시 반환 가능)
for author, book_list in information.items():
    print(f'{author} : {book_list}')
