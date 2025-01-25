# items() 함수는 "딕셔너리"에서 사용. "딕셔너리"의 key - value 값을 "튜플" 형태로 반환


# "딕셔너리 (key - element)" 를 다루는 함수. 딕셔너리의 key와 value를 한번에 반환해준다.

dictA = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
    "key4" : "value4"
}

dictA.items()
result = dictA.items() # 딕셔너리를 튜플 형태로 변환 후 반환
print(result)
print()

for key, element in dictA.items():
    print(f"key {key} : element {element}")