# filter(힘수, 리스트) : 리스트의 요소를 함수에 넣고 True인 것으로, 새로운 리스트 반환

# filter() : 리스트 틍 반복 가능한 자료에서 "조건을 만족하는 요소만 걸러냄"
iterable = []
filter(function, iterable) # function : 각 요소에 대해 T/F를 반환하는 함수

nums = [1, 2, 3, 4, 5, 6]

# 예제.1
even_nums = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums))  # [2, 4, 6]
def func(n):
    return n<3

# 예제.2
input_list = [1,2,3,4,5,6,7,8,9,10]
result_list = filter(func, input_list) # True인 것만 새로운 이터레이터 형태로 반환

print(result_list) # <filter object at 0x1022dabe0>
print(list(result_list)) # [1, 2]


# +) map() 사용시
result_list = map(func, input_list)
print(result_list) # <map object at 0x102755eb0>
print(list(result_list)) # [True, True, False, False, False, False, False, False, False, False]