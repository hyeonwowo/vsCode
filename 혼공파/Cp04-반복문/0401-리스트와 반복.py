# 리스트 선언 및 요소 접근
listA = [1,2,3,4,5]
listB = ["h","e","l","l","o"]
listC = [1,"h",True, 3.14, [1,2,3]]

print(listA)
print(listB)
print(listC)
print()

for element in listA:
    print(element)
print()

for element in listB:
    print(element)
print()

for element in listC:
    print(element)
print()

for element in listC:
    if isinstance(element, list):
        for subElement in element:
            print(subElement)
    else:
        print(element)
print()


# 리스트 인덱스 다루기

listA = [273, 3.14, "string", [1,2,3]]
print(listA[0]) # 273
print(listA[1]) # 3.14
print(listA[2]) # string
print(listA[3]) # [1,2,3]
print()

# 리스트 인덱스 다루기 (음수치사용)
print(listA[-1]) # [1,2,3]
print(listA[-2]) # string
print(listA[-3]) # 3.14
print(listA[-4]) # 273
print()


# 리스트 인덱스 변경

listA[0] = "CHANGED ELEMENT (273 -> string)"
print(listA[0]) # CHANGED ELEMENT
print(listA[1]) # 3.14
print(listA[2]) # string
print(listA[3]) # [1,2,3]
print()

# 리스트 이중 인덱스 사용

listK = [123,"string",[11,22,33],True]
    # print(listK[0][0],listK[0][1],listK[0][2]) - 정수형은 지원하지 않음
print(listK[1][0],listK[1][1],listK[1][2],listK[1][3],listK[1][4],listK[1][5]) # 문자열
print(listK[2][0],listK[2][1],listK[2][2]) # 리스트, 튜플
    # print(listK[3][0],listK[3][1],listK[3][2],listK[3][3]) - Boolean형은 지원하지 않음.


# 리스트 연산: 연결(+), 반복(*), len()

lista = [1,2,3]
listb = [4,5,6]

print("lista : ",lista)
print("listb : ",listb)

print("lista + lista : ",lista+listb)
print("lista * 3 : ",lista * 3)
print("len(lista) : ",len(lista))