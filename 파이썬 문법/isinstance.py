# isinstance : 주어진 객체가 특정 클래스 또는 데이터 타입의 인스턴스인지 확인. -> 객체의 타입을 동적으로 검사 가능.

# ex1)
x = 5
print(isinstance(x, int))  # True

# ex2)
x = 5.0
print(isinstance(x, (int, float)))  # True

# ex3)
x = [1,2,3]
print(isinstance(x, list))

# ex4)
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Animal))  # True
print(isinstance(dog, Dog))     # True
