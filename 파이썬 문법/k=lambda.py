# 정렬, 최소/최대값을 찾을 때 기준을 정하는 용도로 많이 사용


# 기본 예제
nums = [(1,2),(3,1),(5,0)]
sorted_nums = sorted(nums, key=lambda x:x[1]) # 두번째 요소를 기준으로 정렬
print(sorted_nums)
print()

# 문자열 길이를 기준으로 정렬
words = ["asdf","as","a","asdfasdf"]
sorted_words = sorted(words, key=lambda x:len(x))
print(sorted_words)
print()


# 실습 1 : 순서 기준 정렬
nums = [(1,3),(2,2),(3,1)]
result1 = sorted(nums, key=lambda x:x[0])
result2 = sorted(nums, key=lambda x:x[1])

print(result1)
print(result2)


# 실습 2 : 문자열 짧은 순으로 정렬
words = ["a","aaaaa","aaa","aa","aaaa"]
sorted_lists = sorted(words, key=lambda x:len(x)) # 오름차순(짧은거부터 정렬)
sorted_listss = sorted(words, key=lambda x:-len(x)) # 내림차순(긴거부터 정렬)
print(sorted_lists)
print(sorted_listss)
