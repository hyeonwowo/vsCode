# 1,2,3,4,5,6,7 중의 숫자 중에서, 중복 없이 3개 선택

N = 7
M = 3

path = []

def backtrack(start):
    if len(path) == M:
        print(path)
        return
    else:
        for i in range(start,N+1):
            path.append(i)
            backtrack(i+1)
            path.pop()

backtrack(1)
print()


# 1,2,3,4 숫자 중에서, 중복 없이 3개를 순서 있게 골라 모든 경우 출력
N = 4
M = 3

path = []
visited = [False] * (N+1) # 순열에선 visited 필요

def backtrack():
    if len(path) == M:
        print(path)
        return
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack()
            path.pop()
            visited[i] = False
            
backtrack()
print()

# ✨ 조합과 순열의 비교 요약
# 항목 | 조합 | 순열
# 중복방지 방법 | start 인덱스를 넘겨줌 | visited 배열 사용
# 순서 중요성 | 순서 상관 없음 | 순서 중요
# 예시 | [1,2] == [2,1] | [1,2] ≠ [2,1]


# 1,2,3의 부분집합 고르기
N = 3

def backtrack(idx):
    if idx == N:
        print(path)
        return
    
    # idx번째 원소 선택
    path.append(idx+1)
    backtrack(idx+1)
    path.pop()
    
    # idx번째 원소를 고르지 않는다
    backtrack(idx+1)
    
backtrack(0)