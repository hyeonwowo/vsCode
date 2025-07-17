import sys # 길이가 M인 수열을 모두 구하는 프로그램

N,M = map(int, sys.stdin.readline().split())
visited = [False] * (N+1)
path = []

def backtrack():
    if len(path) == M:
        print(*path)
        return
    for i in range(1,N+1):
        if not visited[i]:
            path.append(i)
            visited[i] = True
            backtrack()
            path.pop()
            visited[i] = False
        
backtrack()

# 입력
# 4 2

# 출력
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3