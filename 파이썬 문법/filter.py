# filter(힘수, 리스트) : 리스트의 요소를 함수에 넣고 True인 것으로, 새로운 리스트 반환

def func(n):
    return n<3

input_list = [1,2,3,4,5,6,7,8,9,10]
result_list = filter(func, input_list) # True인 것만 새로운 이터레이터 형태로 반환

print(result_list) # <filter object at 0x1022dabe0>
print(list(result_list)) # [1, 2]


# +) map() 사용시
result_list = map(func, input_list)
print(result_list) # <map object at 0x102755eb0>
print(list(result_list)) # [True, True, False, False, False, False, False, False, False, False]