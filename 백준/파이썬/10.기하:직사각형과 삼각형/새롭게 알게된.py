# min(iterable, key=함수)

# 예제1) 숫자 리스트에서 절댓값이 가장 작은 수 찾기
nums = [-10,5,-3,8]
min_num = min(nums, key=abs)
print(min_num)


# 예제2) 딕셔너리에서 가장 작은 Value의 key구하기
dictA = {
    'a':10,
    'b':3,
    'c':7
}
min_key = min(dictA, key=dictA.get) # min은 기본적으로 dictA의 key들인 'a','b','c'를 iterable로 받음
# key=dictA.get은 내부적으로 하단과 같은 비교 수행
# 'a' - dictA.get('a') -> 10
# 'b' - dictA.get('b') -> 3
# 'c' - dictA.get('c') -> 7
print(min_key)


# dictA.get : 딕셔너리에서 특정 key에 해당하는 Value를 안전하게 가져옴
key = 'a' # 값을 찾고 싶은 Key
default = 0 # key가 없을 때 반환할 기본값(없으면 None)
value = dictA.get(key, default)


# key : 비교시 어떤 기준으로 비교할지 정해줌. 일종의 변환기
min(nums, key = abs) # 절댓값 기준 비교
min(dictA, key=dictA.get) # value 기준으로 Key 비교
words = ["apple","banana","cherry","lemon"]
sorted(words, key = len) # 단어 길이 기준 정렬
