# map() 함수와 filter() 함수

def power(item):
    return item*item
def under_3(item):
    return item<3

list_input_a = [1,2,3,4,5]

    # map(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값으로, 새로운 리스트 반환
    # filter(힘수, 리스트) : 리스트의 요소를 함수에 넣고 True인 것으로, 새로운 리스트 반환


output_a = map(power, list_input_a) # power 함수에 list를 넣어 반환해줌.
print(output_a)
print(list(output_a))
print()

output_b = filter(under_3,  list_input_a) # under_3 함수에 list를 넣어 True인 값만 넣어 반환해줌.
print(output_b)
print(list(output_b))
print()