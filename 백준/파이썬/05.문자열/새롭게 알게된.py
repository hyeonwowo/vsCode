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


# N = input() 사용시 N은 문자열의 형태
N = int(input()) # 정수로 사용하고 싶으면 변환해줘야함
