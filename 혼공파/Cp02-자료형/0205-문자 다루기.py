# 대소문자 변환 lower() upper()

stringa = "HELLO world hello WORLD"
stringA = stringa.upper()

print(stringa.upper())
print(stringA)
print()

stringb = "HELLO world hello WORLD"
stringB = stringb.lower()

print(stringb.lower())
print(stringB)
print()

stringc = "TEST MESSAGE"
stringc.upper()
print(stringc)

# 파괴적함수, 비파괴적함수
    #비파괴적함수
s = "Hello, World"
new_s = s.upper() # s에 upper()을 첨부해도 s는 변하지 않음

print(s) # "Hello, World" (원본 유지)
print(new_s) # "HELLO, WORLD" (새 문자열 반환)
print()

    #파괴적함수
lst = [1,2,3] # 1,2,3
print(lst)
lst.append(4) # 1,2,3,4 - 원본 리스트 변경
print(lst)
print()

# 문자열 양옆 공백제거

input_a = """ 
testmessage1
testmessage2
testmessage3
""" # 맨 윗줄, 아랫즐 공백.

print(input_a) # 공백 제거 전
print()
print(input_a.strip()) # lstrip().rstrip() 함수는 거의 사용하지 않음.
print(input_a) # strip() : 비파괴적 함수
print()
    # 이건 문자열 줄뱌꿈 제거
input_b = """\
testmessage11
testmessage22
testmessage33\
"""
print(input_b)
print()

# 문자열 구성 파악 isOO()

    # isalnum() : 문자열이 알파벳, 숫자로만 구성됐는지 확인
    # isalpha() : 문자열이 알파벳         구성됐는지 확인
    # isdigit() : 문자열이       숫자로만  구성됐는지 확인
    # isspace() : 문자열이 공백으로만      구성됐는지 확인
    # islower() : 문자열이 소문자로만       구성됐는지 확인
    # isupper() : 문자열이 대문자로만       구성됐는지 확인
    # isdecimal() : 문자열이 정수 형태인지 확인

print("TrainA10".isalnum()) # "asdf".alOO() 형태로 변수사용없이 바로 사용 가능.
print("10".isdigit())
print("abcd".isalpha())
print()

# 문자열 찾기 find(), rfind()
output_a = "hellohelloworld".find("hello")
print(output_a) # 첫번째 hello의 가장 앞글자 [0] 출력

output_b = "hellohelloworld".rfind("hello")
print(output_b) # 오른쪽에서 탐색 시작, 두번째 hello의 가장 앞글자 [5] 출력
print()


# 문자열과 in 연산자
print("\"hello\" in \"hello world\" : ","hello" in "hello world")
print("\"hello\" in \"world\" : ","hello" in "world")
print()


# 문자열 자르기 split()
a = "10 20 30 40 50".split(" ") # 반환 결과로 리스트 ['10','20','30','40','50'] 출력
print(a)

b = "10,20,30,40,50".split(",")
print(b)


