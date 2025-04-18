# <주요 문자열 판별 메서드>
# 메서드 | 설명 | 예시
# str.isdigit() | 문자열이 숫자로만 이루어졌는지 |
# str.isalpha() | 문자열이 알파벳으로만 이루어졌는지 |
# str.isalnum() | 문자열이 알파벳 또는 숫자로 이루어졌는지 | 
# str.islower() | 모든 문자가 소문자인지 | 
# str.isupper() | 모든 문자가 대문자인지 |
# str.isspace() | 모든 문자가 공백 문자인지 (' ', \t, \n) |

s1 = "123"
s2 = "abc"
s3 = "abc123"
s4 = "HELLO"
s5 = " "

print(s1.isdigit())   # True
print(s2.isalpha())   # True
print(s3.isalnum())   # True
print(s4.isupper())   # True
print(s5.isspace())   # True
