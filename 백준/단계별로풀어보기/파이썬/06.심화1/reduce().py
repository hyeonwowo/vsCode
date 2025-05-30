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