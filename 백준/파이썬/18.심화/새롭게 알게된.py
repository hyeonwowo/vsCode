# dict.get(key, defalut) : 딕셔너리에서 key 조회시, key가 있으면 해당 값 반환, 없으면 Defalut 값 반환
dictA = {
    'apple' : 5,
    'banana' : 3,
    'cherry' : 6,
    'lemon' : 1
} 

dictB = {
    1 : 11,
    2 : 22,
    3 : 33,
    4 : 44
}

print(dictA.get('apple'))
print(dictB.get(1))
print(dictA.get('adsfasd'),0)
print(dictB.get(146113,0))
print()


# sorted()
sortdict = sorted(dictA.items(), key=lambda x:(x[1],-len(x[0]),x[0])) # 1.value가 작은 순서부터, 2.단어길이가 큰 순서부터, 3. 알파벳 사전순서
                # items()를 붙여줘야, Key + value 가 관여하는 정렬이 가능하다 (없으면, Key로만 정렬)
print(sortdict) # 여기서 sortdict는 정렬된 딕셔너리가 아니라, 정렬된 튜플들의 리스트이다!


# 튜플로 정렬된 리스트의 출력
print(' '.join(key for key, _ in sortdict)) # 두가지 인자가 저장된 튜플이기에 두개의 인자를 받아줘야함

