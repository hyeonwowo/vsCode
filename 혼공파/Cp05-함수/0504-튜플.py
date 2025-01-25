# 튜플 - 리스트와 비슷하지만 한번 결정된 요소를 바꿀 수 없음.

tuple_test = (10,20,30)

print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])
print()

    # tuple_test[0] = 1 에러발생 ! 튜플은 수정 불가능.

# 리스트와 튜플의 특이한 사용

[a,b] = [10,20]
(c,d) = (10,20)

print("a : ",a)
print("b : ",b)
print("c : ",c)
print("d : ",d)
print()


# 괄호가 없는 튜플 - 튜플은 괄호 없이 선언 가능하다.

tuple_test = 10,20,30,40

print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])
print(tuple_test[3])
print()


# 변수의 값을 교환하는 튜플 - 유용함

a, b = 10, 20
print("change before")
print("a : ",a)
print("b : ",b)
print()

a, b = b, a
print("change after")
print("a : ",a)
print("b : ",b)
print()