# str.split() : 문자열을 특정 구분자를 기준으로 나누어 리스트로 변환. 기본적으로 공백을 기준으로 문자열을 나눔

# 기본 사용법 : split() - 공백 기준
expression = "3 + 5 * (2 - 8)"
tokens = expression.split()
print(tokens)

# 특정 구분자로 분할 : split("구분자") - 구분자 기준
data = "apple,banana,lemon,coconat"
token = data.split(",")
print(token)

# 여러 개의 공백 처리 : split() - split()는 여러 개의 공백을 자동으로 무시하고 분리.
text = "hello       world   !!!!!"
token = text.split()
print(token)

