# 정렬, 최소/최대값을 찾을 때 기준을 정하는 용도로 많이 사용


# 기본 예제
nums = [(1,2),(3,1),(5,0)]
sorted_nums = sorted(nums, key=lambda x:x[1]) # 두번째 요소를 기준으로 정렬
print(sorted_nums) # [(5,0), (3,1), (1,2)]
print()

# 문자열 길이를 기준으로 정렬
words = ["asdf","as","a","asdfasdf"] 
sorted_words = sorted(words, key=lambda x:len(x))
print(sorted_words) # ['a', 'as', 'asdf', 'asdfasdf']
print()

# y축 기준으로 먼저 정렬 후, x축 기준으로 정렬
point = [(5, 3), (6, 1), (1, 2), (2, 3), (1, 1), (4, 1), (3, 1)]
sorted_point = sorted(point,key=lambda x:(x[1],x[0]))
print(sorted_point) # [(1, 1), (3, 1), (4, 1), (6, 1), (1, 2), (2, 3), (5, 3)]

# 실습 1 : 순서 기준 정렬
nums = [(1,3),(2,2),(3,1)]
result1 = sorted(nums, key=lambda x:x[0]) # [(1, 3), (2, 2), (3, 1)]
result2 = sorted(nums, key=lambda x:x[1]) # [(3, 1), (2, 2), (1, 3)]

print(result1)
print(result2)


# 실습 2 : 문자열 짧은 순으로 정렬
words = ["a","aaaaa","aaa","aa","aaaa"]
sorted_lists = sorted(words, key=lambda x:len(x)) # 오름차순(짧은거부터 정렬) : ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
sorted_listss = sorted(words, key=lambda x:-len(x)) # 내림차순(긴거부터 정렬) : ['aaaaa', 'aaaa', 'aaa', 'aa', 'a']
print(sorted_lists)
print(sorted_listss)
