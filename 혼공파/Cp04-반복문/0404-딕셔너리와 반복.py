# 딕셔너리 : key 값을 기준으로 저장 (list는 index 번호 기준으로 저장)

# 딕셔너리의 선언 및 출력

dictA = {
    1 : "one",
    2 : "two",
    3 : "three"
}

print(dictA[1])
print(dictA[2])
print(dictA[3])
print()


# 딕셔너리 value값 변경

dictA[1] = "하나"
print(dictA[1])
print()

# 딕셔너리 요소 추가

dictB = {}

dictB["name"] = "son"
dictB["number"] = 7
dictB["grade"] = 9.8

print(dictB)
print(dictB["name"])
print(dictB["number"])
print(dictB["grade"])
print()

    # 딕셔너리 요소 수정
dictB["grade"] = 7.5
print(dictB)
print()


# 딕셔너리 요소 제거

del dictB["name"] # name - son : key - value 전체를 완전히 제거
print(dictB)
print()

# in 키워드

dictC = {
    "key1" : 1,
    "key2" : 2,
    "key3" : 3
}

if "key1" in dictC:
    print(dictC["key1"])

if "key11" in dictC:
    print(dictC["key11"]) # 만약 유효하지 않은 key 접근시 오류 출력 (해당 코드는 if문으로 막아뒀기 때문에 괜찮음.)
else:
    print("Not vaild key, insert key")
    dictC["key11"] = 11

print(dictC)
print()


# get() 함수 : dict.get("key")

dictTOT = {
    "name" : "son",
    "number" : 7,
    "grade" : 8.7
}

value = dictTOT.get("name")
value2 = dictTOT.get("contry")

print(value) # "name" key는 존재하기에 "son" value 값 출력
print(value2) # "contry" key는 존재하지 않기에 None value 값 출력
print()


# for 반복문과 딕셔너리

dictP = {
    "name" : ["son","kane","kross","benzema"],
    "number" : [7,10,8,9],
    "job" : "player"   
}

for key in dictP:
    print(key," : ",dictP[key])