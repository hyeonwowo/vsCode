# for 반복문 : 리스트와 함께 사용

    # for 반복자 in 반복할 수 있는 것
listA = [1,2,3,4,5]

for element in listA:
    print(element)
print()

# 중첩 리스트와 중첩 반복문

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

for smallList in lista:
    print(smallList)

print()

for smallList in lista:
    for element in smallList:
        print(element)
print()


# 전개 연산자 : *listA

a = [1,2,3,4]
b = [*a, *a] # *a는 리스트 전체를 의미함.
c = [a,a]
d = [a+a]

print(b) # [1, 2, 3, 4, 1, 2, 3, 4] : 전개 연산자를 사용해야 원하는 출력값이 나온다.
print(c) # [[1, 2, 3, 4], [1, 2, 3, 4]]
print(d) # [[1, 2, 3, 4, 1, 2, 3, 4]]
print(a+a) # [1, 2, 3, 4, 1, 2, 3, 4] : print(a + a) 를 사용해도 원하는 출력값이 나온다.
print()

# 전개 연산자 : append()와 비파괴적 사용

a = [1,2,3,4]
a.append(5)
print(a)

    # 전개 연산자 사용
b = [1,2,3,4]
c = [*b,5]
print(b)
print(c)