# random.random()은 0이상 1미만의 실수를 반환하는 함수

import random

print(random.random())
print()


# random.randint(a,b) : a이상 b이하의 정수 생성
print(random.randint(0,10)) # 0,1,2,3,4,5,6,7,8,9,10 중 랜덤 정수 생성
print()


# random.uniform(a,b) : a이상 b이하의 실수 생성
print(random.uniform(0,10))
print()

# 리스트에서 랜덤 선택

# 1) random.choice(lista) : 리스트에서 랜덤 요소 1개 선택
# 2) random.choices(lista, k=n) : 리스트에서 중복 허용하여 n개 선택
# 3) random.sample(lista, k=n) : 리스트에서 중복 없이 n개 선택

lista = ['apple', 'banana', 'cherry', 'date']

print(random.choice(lista))    # 'banana'
print(random.choices(lista, k=2))  # ['apple', 'cherry'] (중복 가능)
print(random.sample(lista, k=2))   # ['date', 'banana'] (중복 없음)
print()


# random.shuffle(lista) : 리스트 요소 섞기
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # 예: [3, 1, 5, 2, 4]
print()

