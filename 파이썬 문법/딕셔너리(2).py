students = [
    {"name":"benzema","number":9,"grade":9.2},
    {"name":"ronaldo","number":7,"grade":9.4},
    {"name":"bale","number":16,"grade":7.2},
    {"name":"bale","number":11,"grade":8.7},
]

# 출력방법 1) - 한줄로 출력
print(students)
print()

# 출력방법 2) - 여러줄로 출력
def print_element(a):
    for element in a:
        print(element)
    print()


# 이름 기준 오름차순 정렬 (단일 조건 정렬)
result = sorted(students,key=lambda x:x["name"]) # 정렬한 데이터를 새롭게 받아줘야한다.
print_element(result)
print_element(students) # 기존 데이터는 sorted를 해도 변함 없음


# 이름 -> 번호 순으로 정렬 (다중 조건 정렬)
result2 = sorted(students, key=lambda x:(x["name"],x["number"]))
print_element(result2)


# sorted 사용시 새로운 데이터로 받아줘야함

lista = [5,4,3,2,1]

print(lista)
k = sorted(lista) # 이와 같이 k로 받아줘야함
print(k)