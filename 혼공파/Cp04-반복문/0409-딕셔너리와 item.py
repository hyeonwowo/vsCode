# 딕셔너리와 item() - 딕셔너리 요소를 "튜플" 형태로 반환
    # 튜플 - 수정이 불가하단 점을 제외하면, 리스트와 상당히 비슷.

# items() 함수와 반복문 조합

dictE = {
    "keyA" : "valueA",
    "keyB" : "valueB",
    "keyC" : "valueC",
    "keyD" : "valueD",
}


result = dictE.items()
print(result)
print()

for key, element in dictE.items():
    print(f"key {key} : element {element}")