# 딕셔너리 - Value or key 값에 따른 정렬
    
word = {'B': 2, 'A': 5, 'C': 1}

# key 기준 정렬
sorted_by_key = sorted(word.items(), key=lambda x: x[0])
print(sorted_by_key)

# value 기준으로 내림차순 정렬
sorted_word = sorted(word.items(), key=lambda x: x[1], reverse=True)
print(sorted_word)


# replace() : 문자열을 끝까지 탐색해 치환

def modricAlpha(st):
    dictlist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    
    for key in dictlist:
        st = st.replace(key, " ")  # 해당 패턴을 공백(또는 한 글자)으로 치환

    return len(st.replace(" ", "")) + st.count(" ")  # 실제 글자 수 + 치환된 개수