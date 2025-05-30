import sys

def backtracking(start):
    if len(path) == M:
        print(*path)
        return
    else:
        for i in range(start, N+1):
            path.append(i)
            backtracking(i)
            path.pop()

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    path = []
    backtracking(1)