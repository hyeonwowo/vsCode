import sys # N개중 M개를 고른 수열. 같은수 여러번 가능, 비내림차순

def backtracking(start):
    if len(path) == m:
        if tuple(path) not in log:
            log.append(tuple(path))
            print(*path)
        return
    for i in range(start, n):
        path.append(lst[i])
        backtracking(i)  # 중복 선택 허용 → i부터 다시 탐색
        path.pop()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = sorted(list(map(int, sys.stdin.readline().split())))  # 사전순 보장 위해 정렬
    path = []
    log = []  # 중복 수열 기록용
    backtracking(0)

# 입력
# 4 2
# 9 7 9 1

# 출력
# 1 1
# 1 7
# 1 9
# 7 7
# 7 9
# 9 9