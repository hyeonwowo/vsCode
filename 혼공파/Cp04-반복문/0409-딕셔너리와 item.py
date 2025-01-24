# 딕셔너리와 item()

# items() 함수와 반복문 조합

dictE = {
    "keyA" : "valueA",
    "keyB" : "valueB",
    "keyC" : "valueC",
    "keyD" : "valueD",
}

    # item() 함수 결과 출력

print(dictE.items())
print()

    # for 반복문과 items() 함수 조합 사용
    
for key, element in dictE.items():
    print(f"key - {key} : value - {element}")
print()

