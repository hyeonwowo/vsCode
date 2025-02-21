# insertion - stable
# selection - unstable

students = [
    {"이름": "Furia", "학년": 1, "성적": "A", "전화번호": "766-093-9873", "주소": "101 Brown"},
    {"이름": "Kanaga", "학년": 3, "성적": "B", "전화번호": "898-122-9643", "주소": "22 Brown"},
    {"이름": "Rohde", "학년": 2, "성적": "A", "전화번호": "232-343-5555", "주소": "343 Forbes"},
    {"이름": "Gazsi", "학년": 4, "성적": "B", "전화번호": "766-093-9873", "주소": "101 Brown"},
    {"이름": "Chen", "학년": 3, "성적": "A", "전화번호": "991-878-4944", "주소": "308 Blair"},
    {"이름": "Fox", "학년": 3, "성적": "A", "전화번호": "884-232-5341", "주소": "11 Dickinson"},
    {"이름": "Andrews", "학년": 3, "성적": "A", "전화번호": "664-480-0023", "주소": "097 Little"},
    {"이름": "Battle", "학년": 4, "성적": "C", "전화번호": "874-088-1212", "주소": "121 Whiteman"},
]

# 이름 기준 오름차순 정렬 (단일 조건 정렬)
print("# 이름 기준 오름차순 정렬 (단일 조건 정렬)")
result = sorted(students, key=lambda x: x["이름"])
for student in result:
    print(student)
print()


# 이름 -> 학년 기준 오름차순 정렬 (다중 조건 정렬)
print("# 이름 -> 학년 기준 오름차순 정렬 (다중 조건 정렬)")
result = sorted(students, key=lambda x: (x["이름"], x["학년"]))
for student in result:
    print(student)