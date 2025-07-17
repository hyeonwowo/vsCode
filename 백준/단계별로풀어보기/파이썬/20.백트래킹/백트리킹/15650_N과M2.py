N, M = map(int, input().split())  # 중복 없고 오름차순 수열
path = []
visited = [False] * (N + 1)  # 1번 ~ N번까지 방문 기록 (0번은 사용 안함)

def backtrack(start):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start + 1, N + 1):  # start보다 큰 수만 선택 (오름차순)
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack(i)  # 🔴 인자 `i`를 넘겨야 함
            path.pop()
            visited[i] = False

backtrack(0)  # 처음엔 0부터 시작 (0보다 큰 수: 1,2,3,...부터 시작 가능)


# 입력
# 4 2

# 출력
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4