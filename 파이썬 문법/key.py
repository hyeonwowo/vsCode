# key= : min() max() sorted() 같은 함수에 등장하는 key= 는 비교나 정렬시 기준이 되는 값을 계산하는 함수를 지정하는 파라미터
# key= : 함수를 받는 인자라고 생각해주면 됨

# 1) 문자열 리스트 정렬(길이기준)
words = ['apple','banana','kiwi']
sorted_words = sorted(words, key=len)
min_word = min(words, key=len)
print(sorted_words)
print(min_word)


# 2) 딕셔너리에서 가장 작은 value를 갖는 key 탐색
dictA = {
    'a':100,
    'b':50,
    'c':75
}
min_key = min(dictA, key=dictA.get)


# 3) lambda와 함께 쓰기
students = [
    {'name': 'Alice', 'score': 91},
    {'name': 'Bob', 'score': 87},
    {'name': 'Charlie', 'score': 93}
]
top_student = max(students, key=lambda x:x['score'])
top_studentt = min(students, key=lambda x:x['name'])
print(top_student)
print(top_studentt)