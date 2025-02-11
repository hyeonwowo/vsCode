# enumerate() 함수와 반복문 조합 - enumerate(lista)는 인덱스와 요소를 같이 반환해준다
# ex) print(list(enumerate(lista)))
# ex) for index, element in enumerate(lista):
#         print(f"{index}{element}")

liste = ["element1", "element2", "element3"]

    # 출력 예시

    # 0 번째 요소는 A   
    # 1 번째 요소는 B
    # 2 번째 요소는 C


# case(1) - 번거로움..

i = 0
for item in liste:
    print(f"{i} 번째 요소는 {item}")
    i += 1
print()

# case(2) - 번거로움..

for i in range(len(liste)):
    print(f"{i} 번째 요소는 {liste[i]}")
print()


# enumerate() 함수와 리스트

print(enumerate(liste))
print()
print(list(enumerate(liste)))
print()

for i, value in enumerate(liste): # i - 인덱스넘버, value - list[i]
    print(f"{i} 번째 요소는 {value}")
print()