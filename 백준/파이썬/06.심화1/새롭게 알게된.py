# 딕셔너리 - Value or key 값에 따른 정렬
    
word = {'B': 2, 'A': 5, 'C': 1}

# key 기준 정렬
sorted_by_key = sorted(word.items(), key=lambda x: x[0])
print(sorted_by_key)

# value 기준으로 내림차순 정렬
sorted_word = sorted(word.items(), key=lambda x: x[1], reverse=True)
print(sorted_word)