# enumerate() 함수와 반복문 조합 - 순서가 있는 자료구조 처리시, 인덱스 넘버와 함께 반환.

liste = ["element1", "element2", "element3"]

    # 출력 예시

    # 0 번째 요소는 A   
    # 1 번째 요소는 B
    # 2 번째 요소는 C


# case(1)

i = 0
for item in liste:
    print(f"{i} 번째 요소는 {item}")
    i += 1
print()

# case(2)

for i in range(len(liste)):
    print(f"{i} 번째 요소는 {liste[i]}")
print()


# enumerate() 함수와 리스트

print(enumerate(liste))
print()
print(list(enumerate(liste)))
print()

for i, value in enumerate(liste):
    print(f"{i} 번째 요소는 {value}")
print()