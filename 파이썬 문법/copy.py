# 파이썬의 .copy() 메서드는 리스트[], 딕셔너리{}, 집합{} 에서 사용 (튜플())
# 내부 요소가 변경가능한 객체라면, 그 내부 객체는 여전히 공유됨.


# 1) 리스트에서 .copy()
original_list = [1,2,[3,4]]
copied_list = original_list.copy()

copied_list[0] = 99 # 얕은 복사라서 원본에는 영향 없음.
copied_list[2][0] = 100 # 내부 리스트는 공유됨

original_list = [1, 2, [3, 4]]
copied_list = original_list.copy()

# 값 변경 테스트
copied_list[0] = 99  # 얕은 복사라서 원본에는 영향 없음
copied_list[2][0] = 100  # 내부 리스트는 공유됨

print("Original:", original_list)  # [1, 2, [100, 4]]
print("Copied:", copied_list)      # [99, 2, [100, 4]]

    # 주의) 리스트 내부의 가변 객체(리스트, 딕셔너리)는 공유되므로, 이를 완전히 분리하려면 deepcopy() 사용

# 2) 딕셔너리에서 .copy()
original_dict = {'a':1,'b':[2,3]}
copied_dict =  original_dict.copy()

copied_dict['a'] = 99
copied_dict['b'][0] = 100

print("Original:", original_dict)  # {'a': 1, 'b': [100, 3]}
print("Copied:", copied_dict)      # {'a': 99, 'b': [100, 3]}

    # 주의) 딕셔너리 내부의 가변 객체(리스트, 딕셔너리)는 공유되므로, 이를 완전히 분리하려면 deepcopy() 사용


# 3) 집합에서 .copy()
original_set = {1,2,3}
copied_set = original_set.copy()

copied_set.add(99)

print("Original:", original_set)  # {1, 2, 3}
print("Copied:", copied_set)      # {1, 2, 3, 99}

    # 집합은 내부에 변경 가능한 객체를 가질 수 없으므로, 일반적으로 얕은 복사만으로 충분


# 4) 깊은 복사가 필요할 때 copy.deepcopy()
import copy

original = [[1,2],[3,4]]
deep_copied = copy.deepcopy(original)

deep_copied[0][0] = 99

print("Original:", original)  # [[1, 2], [3, 4]]
print("Deep Copied:", deep_copied)  # [[99, 2], [3, 4]]

    # 깊은 복사 (deepcopy)를 하면 내부 리스트까지 새로운 객체로 복사되어 원본에 영향을 주지 않습니다.