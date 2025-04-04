# 문자열뒤집기

# 1. 슬라이싱 사용 [::-1]
s = "abc"
st = s[::-1]
print(st)


# 2. reverse()함수 + join()
s = "abc"
st = ''.join(reversed(s))
print(st)

# 3. 반복문 사용 (직접 뒤집기)
s = "abc"
reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s
print(reversed_s)  # 출력: cba


# 4. 리스트로 바꿔서 뒤집기
s = "abc"
lst = list(s)
lst.reverse()
reversed_s = ''.join(lst)
print(reversed_s)  # 출력: cba
