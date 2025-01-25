# 함수의 기본 (일반(value) - 가변(*value) - 기본(n=x) 해당 순서로 매개변수 할당) 

def print_n_times(value,n):
    for i in range(n):
        print(value)

print_n_times("hello",5)


# 가변 매개변수 함수

def print_n_times(n, *values): # value에는 문자열이 몇개가 들어가든 상관 없음. list형태로 입력됨.
    for i in range(n): # 전체 반복 횟수 (*values 반복 횟수)
        for value in values:
            print(value)
        print()

print_n_times(3, "hello", "world","!","test","message")
        

# 기본 매개변수 함수

def print_n_times(*values, n=2): # n = 2 사용
    for i in range(n):
        for value in values:
            print(value)
    

print_n_times("hello","test message")


# 키워드 매개변수 함수

def print_n_times(*values, n=2): # n=2 값을, 키워드 매개변수 n=3을 이용해 3번 반복으로 바꿔줌.
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("hello","world!",n=3)


# 기본 매개변수 중에서 필요한 값만 입력

def test(a, b=10, c=100):
    print(a + b + c)

test(10,20,30) # 1) 기본형태 : a=10 ,b=20 ,c=30 - 60
test(a=10, b=100, c=200) # 2) 키워드 매개변수로 모든 매개변수 지정 : a=10 ,b=100 ,c=200 - 110
test(c=10,a=100,b=200) # 3) 키워드 매개변수로 모든 매개변수를 마구잡이로 지정 : a=100 ,b=200 ,c=10  - 310
test(10,c=200) # 4) 키워드 매개변수로 일부 매개변수만 지정 : a=10 ,b=10 ,c=100 - 220