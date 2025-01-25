# 리스트 요소 추가 및 제거 : append(), insert()

    # 리스트명.append(요소)
    # 리스트명.insert(위치, 요소)

lista = [1,2,3]

    # 리스트 "뒤"에 요소 추가
lista.append(4) # 1,2,3,4
print(lista)
lista.append(5) # 1,2,3,4,5
print(lista)
lista.append(6) # 1,2,3,4,5,6
print(lista)
print()

    # 리스트 "중간"에 요소 추가
lista.insert(0,00)
print(lista)
lista.insert(1,11)
print(lista)
lista.insert(2,22)
print(lista)
lista.insert(3,33)
print(lista)
lista.insert(4,44)
print(lista)
lista.insert(5,55)
print(lista)
print()


# 한번에 여러 요소 출력

lista = [1,2,3]
lista.extend([4,5,6]) # 1,2,3 + 4,5,6 (맨 뒤에 요소 추가)
print(lista)
print()

    # 리스트 연결 연산자와 요소 추가의 차이
listA = [1,2,3]
listb = [4,5,6]
print(listA + listb)
listA.extend(listb) # print(listA.extend(listb)) 는 안됨.
print(listA)
print()

# 인덱스로 제거 : del(), pop()

    # del 리스트명[위치]
    # 리스트명.pop(위치) - (위치) 없을 시 마지막 요소 제거.
    
    # [SUM]
    # 단순히 요소를 삭제하려면 "del"
    # 요소를 삭제하면서 그 값을 활용하려면 "pop"
    # pop은 인덱스를 생략할 수 있다는 점에서 더 유연하지만, 슬라이스 삭제는 del만 가능합니다.

lista = [1,2,3,4,5,6]

    # del listA[index]
del lista[0] # 첫번째 리스트 인덱스 제거 - 1
print(lista)

del lista[0] # 첫번째 리스트 인덱스 제거 - 2
print(lista)


    # listA.pop() 매개변수 없을 시 마지막 요소 제거
lista.pop()
print(lista)

lista.pop()
print(lista)

lista.pop(0) # 첫번째 요소 제거
print(lista)

lista.pop(0) # 첫번째 요소 제거
print(lista)


# del 키워드 응용

listA = [1,2,3,4,5,6,7,8,9]
del listA[3:6] # 3~5까지 제거

del listA[4:] # 4부터 끝까지 제거
del listA[:3] # 0부터 2까지 제거




# 값으로 제거하기 : remove()

listc = [1,2,3,4]
listc.remove(1)

listd = [1,2,1,3]
listd.remove(1) # 이런 경우 앞쪽의 1 하나만 지워지고, 두번째 1 은 지워지지 않음 -> for, while 사용

# 모두 제거하기 : clear()

listc.clear()


# 리스트 정렬하기 : sort()

liste = [3,6,8,2,9,1,5,3,7]
liste.sort() # 오름차순 정렬
print(liste)

listf = [3,6,2,7,8,2,1,7,4]
listf.sort(reverse = True) # 내림차순 정렬
print(listf)
print()

# 리스트 내부에 값이 있는지 확인 : in / not in 연산자.

lista = [5,4,2,7,1]

print(5 in lista)
print(100 in lista)

