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