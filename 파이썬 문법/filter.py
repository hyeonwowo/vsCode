# filter(힘수, 리스트) : 리스트의 요소를 함수에 넣고 True인 것으로, 새로운 리스트 반환

def func(n):
    return n<3

input_list = [1,2,3,4,5,6,7,8,9,10]
result_list = filter(func, input_list)

print(result_list)
print(list(result_list))