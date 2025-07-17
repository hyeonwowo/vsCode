import sys # 중복 가능 비내림차순 수열

N,M = map(int, sys.stdin.readline().split())

path = []

def backtrack(start):
    if len(path) == M:
        print(*path)
        return
    else:
        for i in range(start, N+1):
            path.append(i)
            backtrack(i)
            path.pop()

if __name__ == "__main__":
    backtrack(1)
    
# 입력
# 4 2

# 출력
# 1 1
# 1 2
# 1 3
# 1 4
# 2 2
# 2 3
# 2 4
# 3 3
# 3 4
# 4 4