# 파이썬의 set은 중복을 허용하지 않는 데이터구조, 수학적 집합 연산 수행 가능





# set 생성 : set = {}
set1 = {1,2,3,4,4} # 자동으로 중복된 4 하나가 제거된다
set2 = set({1,2,3,4,4}) # 자동으로 중복된 4 하나가 제거된다
print(set1, set2)



# 기본 연산
set1 = {1,2,3}
set1.add(4)
set1.remove(2) # 특정 요소 제거, 없으면 오류
set1.discard(99) # 특정 요소 재거, 없어도 오류 없음
set1.pop() # 임의의 요소 제거(set은 순서가 없으므로 무작위로 제거됨)
set1.clear() # 모든 요소 제거



# 집합 연산
A={1,2,3,4}
B={3,4,5,6}

    # 합집합 (union)
print(A|B)
print(A.union(B))

    # 교집합 (intersection)
print(A&B)
print(A.intersection(B))

    # 차집합 (difference)
print(A-B)
print(A.difference(B))

    # 대칭 차칩잡 (symmetric difference) : 서로 다른 요소만 포함
print(A^B)
print(A.symmetric_difference(B))



# 부분 집합 & 상위 집합 검사
A = {1,2,3}
B = {1,2,3,4,5}

print(A.issubset(B)) # True (A는 B의 부분집합)
print(B.issuperset(A)) # True (B는 A의 상위집합)
print(A.isdisjoint(B)) # False (공통 요소 있음)
print(A.isdisjoint({10,20})) # True (공통 요소 없음)



# set을 활용한 중보 제거
numbers = [1,2,2,3,4,4,5]
unique_numbers = list(set(numbers))
print(unique_numbers)



# set을 이용한 리스트 비교
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

common = set(list1) & set(list2)
print(common)

diff = set(list1) - set(list2)
print(diff)



# set 컴프리헨션
squared_set = {x**2 for x in range(1,6)}
print(squared_set)



# set을 이용한 빠른 검색
data = set(["apple","banana", "cherry"])

print("banana" in data)
print("Lemon" in data)



# set에 리스트 추가
s = {1,2,3}
    #s.add([4,5]) # 오류 발생 ! - set은 변경 불가능한 객체 저장, list는 변경 가능하므로 오류 발생


# 1.리스트를 튜플로 변환하여 추가
s = {1,2,3}
s.add(tuple([4,5]))
print(s)

# 2. set.updatae()를 사용하여 리스트의 개별 요소 추가
s = {1,2,3}
s.update([4,5])
print(s)

# 3. frozenset을 사용하여 리스트를 set에 추가 - frozenset은 변경 불가능한 집합이므로 set에 추가 가능
s = {1,2,3}
s.add(frozenset([4,5]))
print(s)