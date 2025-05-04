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
