# replace() 메소드는 파이썬 문자열에서 아주 자주 쓰이는 강력하고 간단한 도구. 문자열에서 특정 부분을 찾아 다른것으로 바꿀 때 사용

# 1. 단순 문자열 치환
text = "apple banana apple"
new_text = text.replace("apple", "orange")
print(new_text)  # 출력: "orange banana orange"


# 2. 일부만 바꾸기 (count 사용)
text = "apple apple apple"
new_text = text.replace("apple", "orange", 2)
print(new_text)  # 출력: "orange orange apple"


# 3. 공백 / 특수문자 제거
s = "hello-world"
s = s.replace("-", "")
print(s)  # 출력: "helloworld"


# 4. 크로아티아 문제 응용
s = "ljes=njak"
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatia:
    s = s.replace(c, "*")  # *은 대체용 문자 (한 글자)
print(len(s))  # → 크로아티아 알파벳 개수
