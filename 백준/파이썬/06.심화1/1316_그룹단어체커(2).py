def is_group_word(word):
    seen = set() # list를 사용해도 되지만, 속도가 느리기에 set() 사용 추천 
    prev = ''
    for ch in word:
        if ch != prev:
            if ch in seen:
                return False
            seen.add(ch)
        prev = ch
    return True

def group_word_count(n):
    return sum(
        1 for _ in range(n)
        if is_group_word(input().strip())
    )

if __name__ == "__main__":
    N = int(input())
    print(group_word_count(N))
