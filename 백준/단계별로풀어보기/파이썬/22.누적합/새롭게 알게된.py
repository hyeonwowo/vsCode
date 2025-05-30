# 알파벳 -> 아스키코드 변경
print(ord('A'))  # 출력: 65
print(ord('a'))  # 출력: 97

print(chr(65))  # 출력: 'A'
print(chr(97))  # 출력: 'a'

    # 알파벳 출력 예시
# 대문자 A-Z 출력
for i in range(65, 91):
    print(chr(i), end=' ')  # A B C ... Z

print()

# 소문자 a-z 출력
for i in range(97, 123):
    print(chr(i), end=' ')  # a b c ... z


# lst.index()
lst = [1, 3, 5, 7, 9]
idx = lst.index(3)
print(idx)  # 출력: 1

    # 주의사항 : lst.index(x)는 리스트에 x가 없으면 ValueError 예외를 발생, in 연산자를 먼저 확인
if 3 in lst:
    idx = lst.index(3)
    print(idx)
else:
    print("값이 리스트에 없습니다.")
