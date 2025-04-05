# 딕셔너리 - Value or key 값에 따른 정렬
    
word = {'B': 2, 'A': 5, 'C': 1}

# key 기준 정렬
sorted_by_key = sorted(word.items(), key=lambda x: x[0])
print(sorted_by_key)

# value 기준으로 내림차순 정렬
sorted_word = sorted(word.items(), key=lambda x: x[1], reverse=True)
print(sorted_word)


# replace() : 문자열을 끝까지 탐색해 치환
def modricAlpha(st):
    dictlist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    
    # replace()는 새로운 문자열을 반환
    for key in dictlist:
        st = st.replace(key, " ")  # 해당 패턴을 공백(또는 한 글자)으로 치환

    return len(st.replace(" ", "")) + st.count(" ")  # 실제 글자 수 + 치환된 개수


# filter() : 리스트 틍 반복 가능한 자료에서 "조건을 만족하는 요소만 걸러냄"
iterable = []
filter(function, iterable) # function : 각 요소에 대해 T/F를 반환하는 함수

nums = [1, 2, 3, 4, 5, 6]

# 예제.1
even_nums = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums))  # [2, 4, 6]


# reduce() : 반복 가능한 자료형의 모든 값을 누적하여 하나의 결과 도출

# 1. 누적 덧셈
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda acc, x: acc + x, numbers)
print(result)  # 15


# 2. 누적 곱셈
numbers = [1,2,3,4]
result = reduce(lambda acc, x : acc*x, numbers)
print(result)


# 3. 문자열 연결
chars = ['H', 'e', 'l', 'l', 'o']

word = reduce(lambda acc, x : acc + x, chars)
print(word)


# 4. initializer 사용 예시
numbers = [1,2,3]
result = reduce(lambda acc,x:acc+x,numbers, 10)
print(result) # 10 +1+2+3