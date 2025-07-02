import sys # 자연수 N개 중에서 M개를 고른 수열. 중복되는 수열 안됨

def backtracking():
    if len(path) == m:
        if tuple(path) not in log:  # 중복 확인
            log.add(tuple(path))    # 출력된 조합 기록
            print(*path)
        return
    for i in range(n):
        path.append(lst[i])
        backtracking()
        path.pop()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    path = []
    log = set()  # 중복 검사용, 리스트 대신 set으로!
    backtracking()

# 입력
# 4 2
# 9 7 9 1

# 출력
# 1 7
# 1 9
# 7 1
# 7 9
# 9 1
# 9 7
# 9 9