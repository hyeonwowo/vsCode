# 연속하는 요소가 3개 이상인 인덱스의 처음과 끝 출력
def find_consecutive_ranges(lst, min_length=3):
    if not lst:
        return []
    
    result = []
    start = 0
    count = 1
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            if count >= min_length:
                result.append((start, i - 1))
            start = i
            count = 1
    
    if count >= min_length:
        result.append((start, len(lst) - 1))
    
    return result

# 테스트 코드
lista = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 8]
result = find_consecutive_ranges(lista)
print(result)  # [(2, 4), (6, 10)]
