# dict.get(찾고자 하는 키, 키가 없을 때 반환할 기본값(선택, 생략시 None)) : 딕셔너리에서 값 조회시 사용

d = {
    'apple' : 3,
    'banana' : 5
}

print(d.get('apple'))
print(d.get('orange')) # None (키가 없으면 디폴트로 None 반환)
print(d.get('orange',0)) # 0 (기본값 설정시, 해당키 없으면 기본값 반환)