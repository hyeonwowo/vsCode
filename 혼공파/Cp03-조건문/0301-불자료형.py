# True, False 자료형

print(True)
print(False)
print()

# 비교연산자 - 숫자

print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)
print()

# 비교연산자 - 문자

print("a" == "b")
print("a" != "b")
print("a" < "b")
print("a" > "b")
print("a" <= "b")
print("a" >= "b")
print()

# not 연산자

print(not True)
print(not False)
print()
    # not 연산자 사용 예시
x = 10 < 20
print("10 < 20 : ",x)
print("10 < 20 not : ", not x)

# and , or 연산자

print("True and True : ", True and True)
print("True and False : ", True and False)
print("False and True : ", False and True)
print("False and False : ", False and False)
print()

print("True or True : ", True or True)
print("True or False : ", True or False)
print("False or True : ", False or True)
print("False or False : ", False or False)
print()

# if 조건문
number = int(input("type num data >> "))

if number >0:
    print("number > 0")
elif number == 0:
    print("number == 0")
else:
    print("number < 0")