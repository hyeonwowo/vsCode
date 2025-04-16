# sort()와 sorted()

# sort() : 리스트만 사용 가능, 리스트 객체.sort()
numbers = [3, 1, 4, 2]
numbers.sort() # numbers를 정렬하고, numbers.sort() 자체는 None 반환
print(numbers)


# sorted() : 모든 반복 가능한 객체, sorted(리스트객체)
numbers = [3, 1, 4, 2]
new_numbers = sorted(numbers)
print(numbers)      
print(new_numbers)


# 공통옵션
names = ["apple", "banana", "cherry"]

# 길이 기준 오름차순 정렬
sorted_names = sorted(names, key=len)
print(sorted_names)  # ['apple', 'banana', 'cherry']

# 길이 기준 내림차순 정렬
names.sort(key=len, reverse=True)
print(names)         # ['banana', 'cherry', 'apple']
