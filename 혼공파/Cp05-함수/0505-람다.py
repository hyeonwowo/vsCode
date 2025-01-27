# 람다 - 함수를 간단하고 쉽게 선언하는 방법. (1회용 함수)

def call_3_times(func): # 메개변수로 받은 함수를 10회 호출
    for i in range(3):
        func()

def print_hello():
    print("hello world !")

call_3_times(print_hello)
print()
# 람다 사용 예시 - lambda 매개변수 : 리턴값

power = lambda x: x*x
under_3 = lambda x: x<3

input_list = [1,2,3,4,5]

output_a = map(power, input_list)
print(output_a)
print(list(output_a))
print()

output_b = filter(under_3, input_list)
print(output_b)
print(list(output_b))