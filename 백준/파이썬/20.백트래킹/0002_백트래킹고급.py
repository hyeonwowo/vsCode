# 🎯 조합이란?
# "순서 상관 없이" 정해진 수를 선택하는 것.

# ✅ 예를 들어 1,2,3에서 2개를 고른다고 하면:
# [1,2]와 [2,1]은 같은 조합이다!
# 즉, [1,2]만 세고 [2,1]은 세지 않는다.
# ✨ 조합은 "순서"가 중요하지 않다!!

# 구분 | 예시
# 순열 | [1,2] ≠ [2,1]
# 조합 | [1,2] == [2,1] (같은 것으로 취급)


# 백트래킹으로 조합 만들기
N = 4
M = 2

path = []

def backtrack(start):
    if len(path) == M:
        print(path)
        return
    
    for i in range(start, N+1):
        path.append(i)
        backtrack(i+1)
        path.pop()
        
backtrack(1)
print()


# 1,2,3,4,5 중에서 3개를 순서 상관 없이 고르기 (중복된 숫자가 있으면 안됨)
N = 5
M = 3

path = []
def backtrack(start):
    if len(path) == M:
        print(path)
        return 
    for i in range(start,N+1):
        path.append(i)
        backtrack(i+1)
        path.pop()

backtrack(1)
print()