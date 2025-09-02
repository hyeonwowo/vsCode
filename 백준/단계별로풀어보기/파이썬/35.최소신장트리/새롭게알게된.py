# 소수점 몇째자리 까지 출력
value = 3.141592
print(f"{value:.2f}")  # 3.14


# 간선이 많으면 프림, 적으면 크루스칼
# E ~= V*V : prim, E ~= V : kruskal


# sorted(), .sort()
lst = [5,3,4,2,1]

lst.sort() # 기존 리스트를 정렬된 상태로 바꾼다
print(lst) # [1,2,3,4,5]


lst = [5,3,4,2,1]

new = sorted(lst) # 복사된 정렬 리스트르 반환, 기존 리스트는 변함 없음
print(lst) # [5,3,4,2,1]
print(new) # [1,2,3,4,5]