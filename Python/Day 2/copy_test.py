a = 5
b = a
b = 50
print(a, b)     # 5 50
# b의 변화가 a에 영향을 주지 않음 - b는 a의 값을 받아 새로운 주소에 할당
#                                 (a와 b는 다른 주소를 참조하고 있다.)

# =====================================================================

# 1. 깊은 복사 ()
A = [1, 2, 3]
B = A
B[0] = 100
print(A, B)      # [100, 2, 3] [100, 2, 3]
# B의 변화가 A에도 영향을 줌 - A와 B는 같은 주소를 참조하고 있다


# 2. 얕은 복사 (shallow copy)
aa = [1, 2, 3]
bb = aa[:]                 # 얕은 복사 by 슬라이싱
                           # aa의 값을 받아와 새로운 id에 할당
print(id(aa), id(bb))      # 2517715059072 2517715059328 (aa와 bb는 다른 주소를 참조) 
print(aa == bb)            # True : 값이 동일한지 판별
print(aa is bb)            # False : 주소가 동일한지 판별
bb[0] = 5
print(aa, bb)              # [1, 2, 3] [5, 2, 3]

# =====================================================================

# 2차원 배열
# 1. 얕은 복사====================
AA = [
    [1, 2],
    [3, 4]
]
BB = AA[:]        
# BB = list(AA)
# BB = copy.copy(AA)

print(id(AA), id(BB))           # 2272964457280 2272964457472 (전체 list의 주소는 다름)
print(id(AA[0]), id(BB[0]))     # 2272964455872 2272964455872 (전체 list내의 요소에 대한 주소는 동일)
AA[0][0] = 100                  # [[100, 2], [3, 4]] [[100, 2], [3, 4]]
                                # AA 전체 list 내의 요소에 대한 변경이 BB에도 적용됨 (얕은복사에 의한 오류)
print(AA, BB)

# AA 전체에 대한 복사는 BB 전체의 별도 id를 생성함
# 하지만, AA 내부의 요소에 대해서는 별도의 id 생성 없이 
# BB의 요소가 각각 AA의 [1,2]과 AA의 [3, 4]의 주소를 바라보게 됨 (얕은 복사


# 2. 깊은 복사===========================================================
import copy
Aa = [
    [1, 2],
    [3, 4]
]

Bb = copy.deepcopy(Aa)
Aa[0].append(1)
print(Aa)               # [[1, 2, 1], [3, 4]]
print(Bb)               # [[1, 2], [3, 4]]

# Aa 내의 요소를 변경해도 Bb에 영향 X (깊은 복사)