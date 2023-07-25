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
# 내장 함수 없이 
def remove_duplicates2(lst):
    # 새로운 리스트를 만들고
    new_lst = []
    # 입력받은 리스트를 순회하면서
    for num in lst :
        # new_lst에 없는 수라면
        if num not in new_lst :
            # new_lst에 추가한다
            new_lst.append(num)
    return new_lst

result2 = remove_duplicates2([1, 2, 2, 3, 4, 4, 5])
print(result2)


# set()을 통해서
def remove_duplicates3(lst):
    return list(set(lst))

result3 = remove_duplicates3([1, 2, 2, 3, 4, 4, 5])
print(result3)


# 함수를 통해서 2
def remove_duplicates4(lst):
    # 카운팅 배열을 0으로 초기하
    cnt = [0] * (5+1)    # [0]은 리스트 내의 값을 0으로 초기화 하는 것
                         # 곱하는 수는 리스트 요소가 다 들어갈만큼의 숫자 + 1
    # 카운팅
    for num in lst :
        cnt[num] += 1    # lst를 순회하며, "cnt list의 인덱스"가 num과 같은 칸에 저장된 값을 1 증가
                         # 만약 2가 세번 들어오면 cnt[2]에 저장된 값은 0 -> 1 -> 2 -> 3 증가 

    # counts에서 값이  0이 아닌 인덱스만 lst에 추가
    lst = []
    for i in range(len(cnt)):
        if cnt[i] :            # True일 경우 인덱스 값을 append 하는 것이므로 중복으로 들어온 수도 한번씩만 append됨 
            lst.append(num)
    return lst

result4 = remove_duplicates4([1, 2, 2, 3, 4, 4, 5])
print(result4)