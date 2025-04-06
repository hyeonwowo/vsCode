# 새롭게 알게된
# 1. 리스트 내부 요소 이어붙이기 : join()
# 2. 리스트 내부 요소 개수 확인 : len()
# 3. 문자열 뒤집기 : [::-1]
# 4. 삼항 연산자 : return x if x > y else y

# join
# "구분자".join(리스트 or 이터러블) - 문자열 내의 요소들을 툭정 구분자로 연결하여 하나의 문자열로 리턴
# 요소는 반드시 문자열 !

wordList = ["Test","Message","Fun"]
result = " ".join(wordList)
print(result)

result = "".join(wordList)
print(result)

result = ",".join(wordList)
print(result)

result = "+".join(wordList)
print(result)


# 리스트 요소 확인
lst = [1,2,3] # 입력 세가지 모두가 들어왔나 확인하고 싶을 때
print(len(lst)) # 3

lst = [1,3] # 입력이 두개만 들어옴
print(len(lst)) # 2

lst = [None, None, None]
print(len(lst)) # 3

# N = input() 사용시 N은 문자열의 형태
N = int(input()) # 정수로 사용하고 싶으면 변환해줘야함


# 문자열뒤집기

# 1.슬라이싱 사용 [::-1]
s = "abc"
reversed_s = s[::-1]
print(reversed_s)  # 출력: cba

# 2. reversed()함수 + join()
s = "abc"
reversed_s = ''.join(reversed(s))
print(reversed_s)  # 출력: cba

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


# 삼항 연산자
def df(x,y):
    return x if x>y else y

print(df(2,3))
print(df(3,2))
