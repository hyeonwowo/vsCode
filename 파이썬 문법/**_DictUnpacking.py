# ** - 딕셔너리의 key : value 쌍을 unpacking해서 함수 인자로 전달할 때 사용

# * - 리스트/튜플 등 순차적 자료형
# ** - 딕셔너리 같은 키-쌍 자료형

# 1.함수 인자에 딕셔너리 전달
def greet(name, age):
    return f"{name}-{age}"
info = {
    "kane" : 32,
    "son" : 33
}

greet(**info)

# 2.함수 정의에서 **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
print_info(name="son", age=32, major="CS")

# 3.딕셔너리 병합
a = {'x':1,
     'y':2}
b = {
    'y':100,
    'z':3
}

merged = {**a, **b}
print(merged)