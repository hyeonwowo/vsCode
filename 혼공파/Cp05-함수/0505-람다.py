# 람다 - 함수를 간단하고 쉽게 선언하는 방법. (1회용 함수)

def call_10_times(func): # 메개변수로 받은 함수를 10회 호출
    for i in range(10):
        func()

def print_hello():
    print("hello world !")

call_10_times(print_hello)