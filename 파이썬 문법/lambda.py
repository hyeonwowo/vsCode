# 람다 : 함수를 간단하고 쉽게 선언하는 방법. (1회용 함수) - lambda 매개변수 : 표현식

power = lambda x : x*x
under_3 = lambda x : x<3

input_list = [1,2,3,4,5]

output_a = map(power, input_list) # case 1)
output_a = map(lambda x: x*x, input_list) # case 2) 람다를 map 내부에 바로 선언
print(output_a)
print(list(output_a))
print()

output_b = filter(under_3, input_list) # case 1)
output_b = filter(lambda x: x<3, input_list) # case 2) 람다를 filter 내부에 바로 선언
print(output_b)
print(list(output_b))