students = [
    {"name":"benzema","number":9,"grade":9.2},
    {"name":"ronaldo","number":7,"grade":9.4},
    {"name":"bale","number":11,"grade":8.7}
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