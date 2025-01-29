# .keys() - 딕셔너리의 모든 key 목록 반환

adjacency_list = {
    1: [2, 3],  
    2: [1, 4],  
    3: [1],  
    4: [2]
}

print(adjacency_list.keys()) # 모든 키 [1,2,3,4]를 반환
print()

# .keys()를 활용한 특정 정점 검사

    # 그래프에서 특정 정점 v가 존재하는지 확인할 때 유용함.

v1 = 1
v2 = 7

if v1 in adjacency_list.keys():
    print(f"vertex {v1} in graph.")
print()

if v2 not in adjacency_list.keys():
    print(f"vertex {v2} not in graph.")
print()


# .keys() - 딕셔너리의 모든 key 반환
# .values() - 딕셔너리의 모든 value 반환
# .items() - 딕셔너리의 모든 key,value 반환

print("key : ",adjacency_list.keys()) # key 반환
print("value : ",adjacency_list.values()) # value 반환
print("key,value : ",adjacency_list.items()) # key,value 반환


#dict_keys 객체는 리스트처럼 사용할 수 있지만, list()로 변환하면 실제 리스트로 변환 가능.